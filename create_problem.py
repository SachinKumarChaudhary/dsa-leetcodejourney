#!/usr/bin/env python3
import os, sys, subprocess, requests

# ---------- helpers ----------
def pad(n):
    return f"{int(n):04d}"

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return ""

def get_clipboard():
    return run("termux-clipboard-get")

def fetch_leetcode(slug):
    url = "https://leetcode.com/graphql"
    query = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": slug},
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
            topicTags { name }
          }
        }"""
    }
    try:
        r = requests.post(url, json=query, timeout=10)
        data = r.json()["data"]["question"]
        return data["difficulty"], [t["name"] for t in data["topicTags"]]
    except:
        return "Unknown", []

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ---------- README ----------
def init_readme():
    if not os.path.exists("README.md"):
        with open("README.md", "w") as f:
            f.write("""# 🚀 DSA LeetCode Journey

## 📊 Progress
- Total: 0
- Easy: 0
- Medium: 0
- Hard: 0

---

## 🧠 Approach
- v1 → My original thinking  
- v2 → Improved / optimized  
- v3 → Alternative approach  

---

## 📂 Structure
topic/LC-xxxx-problem/
- v1.py
- v2.py
- v3.py
- notes.md

---

## 🔥 Problems

| ID | Title | Difficulty | Topic | Link |
|----|------|------------|------|------|
""")

def update_readme(num, title, slug, topic, diff):
    init_readme()

    line = f"| LC-{num} | {title} | {diff} | {topic} | https://leetcode.com/problems/{slug}/ |\n"

    with open("README.md", "r") as f:
        content = f.readlines()

    easy = medium = hard = 0

    for l in content:
        if "| LC-" in l:
            if "Easy" in l: easy += 1
            elif "Medium" in l: medium += 1
            elif "Hard" in l: hard += 1

    if diff == "Easy": easy += 1
    elif diff == "Medium": medium += 1
    elif diff == "Hard": hard += 1

    total = easy + medium + hard

    for i, l in enumerate(content):
        if l.startswith("- Total:"):
            content[i] = f"- Total: {total}\n"
        elif l.startswith("- Easy:"):
            content[i] = f"- Easy: {easy}\n"
        elif l.startswith("- Medium:"):
            content[i] = f"- Medium: {medium}\n"
        elif l.startswith("- Hard:"):
            content[i] = f"- Hard: {hard}\n"

    content.append(line)

    with open("README.md", "w") as f:
        f.writelines(content)

# ---------- patterns ----------
def update_patterns(topic, num, title):
    path = "patterns.md"

    entry = f"- LC-{num} → {title}\n"

    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(f"## {topic}\n{entry}")
        return

    with open(path, "r") as f:
        content = f.readlines()

    found = False
    for i, line in enumerate(content):
        if line.strip() == f"## {topic}":
            content.insert(i+1, entry)
            found = True
            break

    if not found:
        content.append(f"\n## {topic}\n{entry}")

    with open(path, "w") as f:
        f.writelines(content)

# ---------- MAIN ----------
def main():
    if len(sys.argv) < 5:
        print("Usage: python create_problem.py <num> <slug> <topic> \"<title>\"")
        return

    num_raw, slug, topic, title = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    num = pad(num_raw)

    base = f"{topic}/LC-{num}-{slug}"
    link = f"https://leetcode.com/problems/{slug}/"

    diff, tags = fetch_leetcode(slug)

    clip = get_clipboard()
    if not clip:
        clip = "class Solution:\n    pass\n"

    header = f"# LC-{num} {title}\n# {link}\n# Difficulty: {diff}\n\n"

    write(f"{base}/v1.py", header + "# v1\n\n" + clip)

    write(f"{base}/v2.py", header + "# v2 (Refined)\n\nclass Solution:\n    pass\n")

    write(f"{base}/v3.py", header + "# v3 (Alternative)\n\nclass Solution:\n    pass\n")

    write(f"{base}/notes.md", f"""# LC-{num} {title}

## Key Insight

## Why my approach worked / failed

## Pattern

## When to use this again
""")

    update_readme(num, title, slug, topic, diff)
    update_patterns(topic, num, title)

    run("git add .")
    run(f'git commit -m "LC-{num}: {title} [{diff}] ({topic})"')

    print(f"Done → {base}")
    print("Run: git push")

if __name__ == "__main__":
    main()
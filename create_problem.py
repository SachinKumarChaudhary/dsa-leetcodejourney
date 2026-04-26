#!/usr/bin/env python3
import os, sys, subprocess, requests

# ---------- helpers ----------
def pad(n): return f"{int(n):04d}"

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return ""

def get_clipboard():
    txt = run("termux-clipboard-get")
    return txt if txt else ""

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
        diff = data["difficulty"]
        tags = [t["name"] for t in data["topicTags"]]
        return diff, tags
    except:
        return "Unknown", []

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ---------- problems.md (full list) ----------
def init_problems_md():
    if not os.path.exists("problems.md"):
        with open("problems.md", "w") as f:
            f.write("""# Problems

| ID | Title | Difficulty | Topic | Link |
|----|------|------------|------|------|
""")

def append_problem(num, title, slug, topic, diff):
    init_problems_md()
    line = f"| LC-{num} | {title} | {diff} | {topic} | https://leetcode.com/problems/{slug}/ |\n"
    with open("problems.md", "a") as f:
        f.write(line)

def read_all_problems():
    if not os.path.exists("problems.md"):
        return []
    rows = []
    with open("problems.md", "r") as f:
        for l in f:
            if l.startswith("| LC-"):
                rows.append(l.strip())
    return rows

# ---------- README dashboard ----------
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

## 🔥 Recent Problems
<!-- recent -->

---

➡️ Full list → problems.md

---

## 🧠 Approach
- v1 → My original thinking  
- v2 → Improved  
- v3 → Alternative  
""")

def update_readme():
    init_readme()
    rows = read_all_problems()

    # stats
    easy = sum(1 for r in rows if "| Easy |" in r)
    med  = sum(1 for r in rows if "| Medium |" in r)
    hard = sum(1 for r in rows if "| Hard |" in r)
    total = len(rows)

    # recent (last 10)
    recent = rows[-10:][::-1]  # latest first
    recent_lines = [f"- {r.split('|')[1].strip()} {r.split('|')[2].strip()}" for r in recent]

    with open("README.md", "r") as f:
        content = f.readlines()

    # update stats
    for i, l in enumerate(content):
        if l.startswith("- Total:"):
            content[i] = f"- Total: {total}\n"
        elif l.startswith("- Easy:"):
            content[i] = f"- Easy: {easy}\n"
        elif l.startswith("- Medium:"):
            content[i] = f"- Medium: {med}\n"
        elif l.startswith("- Hard:"):
            content[i] = f"- Hard: {hard}\n"

    # update recent block
    start = None
    for i, l in enumerate(content):
        if l.strip() == "<!-- recent -->":
            start = i
            break

    if start is not None:
        # remove old recent (until next --- or blank line)
        j = start + 1
        while j < len(content) and not content[j].startswith("---"):
            content.pop(j)
        # insert new recent
        for line in recent_lines:
            content.insert(start + 1, line + "\n")
            start += 1

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

    for i, line in enumerate(content):
        if line.strip() == f"## {topic}":
            content.insert(i + 1, entry)
            break
    else:
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
    write(f"{base}/v2.py", header + "# v2\n\nclass Solution:\n    pass\n")
    write(f"{base}/v3.py", header + "# v3\n\nclass Solution:\n    pass\n")

    write(f"{base}/notes.md", f"""# LC-{num} {title}

## Key Insight

## Why my approach worked / failed

## Pattern

## When to use this again
""")

    append_problem(num, title, slug, topic, diff)
    update_readme()
    update_patterns(topic, num, title)

    print(f"Done → {base}")
    print("Now: git add . && git commit -m 'LC-{num}: {title}' && git push")

if __name__ == "__main__":
    main()
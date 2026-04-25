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
        diff = data["difficulty"]
        tags = [t["name"] for t in data["topicTags"]]
        return diff, tags
    except:
        return "Unknown", []

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[create] {path}")

# ---------- README ----------
def init_readme():
    if not os.path.exists("README.md"):
        with open("README.md", "w") as f:
            f.write("""# DSA Journey

## Stats
- Total: 0
- Easy: 0
- Medium: 0
- Hard: 0

---

## Problems

| ID | Title | Difficulty | Topic | Tags | Link |
|----|------|------------|------|------|------|
""")

def update_readme(num, title, slug, topic, diff, tags):
    init_readme()

    line = f"| LC-{num} | {title} | {diff} | {topic} | {', '.join(tags)} | https://leetcode.com/problems/{slug}/ |\n"

    with open("README.md", "r") as f:
        content = f.readlines()

    # Update stats
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

    print("[update] README")

# ---------- MAIN ----------
def main():
    if len(sys.argv) < 5:
        print("Usage: python create.py <num> <slug> <topic> \"<title>\"")
        return

    num_raw, slug, topic, title = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    num = pad(num_raw)

    base = f"{topic}/LC-{num}-{slug}"
    link = f"https://leetcode.com/problems/{slug}/"

    # fetch metadata
    diff, tags = fetch_leetcode(slug)

    # clipboard
    clip = get_clipboard()
    if not clip:
        clip = "class Solution:\n    def solve(self, n: int):\n        pass\n"

    header = f"""# LC-{num} {title}
# Link: {link}
# Difficulty: {diff}
# Tags: {', '.join(tags)}

"""

    # files
    write(f"{base}/v1.py", header + "# Version: v1 (LeetCode)\n\n" + clip)

    write(f"{base}/v2.py", header + """# Version: v2 (Refined)

class Solution:
    def solve(self, n: int):
        pass
""")

    write(f"{base}/v3.py", header + """# Version: v3 (Alternative)

class Solution:
    def solve(self, n: int):
        pass
""")

    write(f"{base}/notes.md", f"""# LC-{num} {title}

## Key Idea

## Mistake I made

## Pattern
""")

    # update README
    update_readme(num, title, slug, topic, diff, tags)

    # commit
    run("git add .")
    run(f'git commit -m "LC-{num} {title} [{diff}] - {topic}"')

    print(f"\nDone → {base}")
    print("Now run: git push")

if __name__ == "__main__":
    main()
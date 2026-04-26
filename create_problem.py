#!/usr/bin/env python3
import os, sys, subprocess, requests

def pad(n): return f"{int(n):04d}"

def fetch_leetcode(slug):
    url = "https://leetcode.com/graphql"
    query = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": slug},
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }"""
    }
    try:
        r = requests.post(url, json=query, timeout=10)
        return r.json()["data"]["question"]["difficulty"]
    except:
        return "Unknown"

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# ---------- problems.md ----------
def init_problems_md():
    if not os.path.exists("problems.md"):
        with open("problems.md", "w") as f:
            f.write("""# Problems

| ID | Title | Difficulty | Topic | Pattern | Link |
|----|------|------------|------|--------|------|
""")
def infer_pattern(topic, title):
    t = title.lower()

    if topic == "two-pointers":
        return "two pointers"
    if topic == "greedy":
        return "greedy"
    if topic == "arrays":
        return "array manipulation"
    if topic == "strings":
        return "string processing"
    if topic == "math":
        return "math / simulation"

    return ""

def append_problem(num, title, slug, topic, diff):
    init_problems_md()
    pattern = infer_pattern(topic, title)
    line = f"| LC-{num} | {title} | {diff} | {topic} | {pattern} | https://leetcode.com/problems/{slug}/ |\n"

    with open("problems.md", "r", encoding="utf-8") as f:
        existing = f.read()

    if f"LC-{num}" in existing:
      print("⚠️ Problem ID already exists, skipping append...")
      return False

    with open("problems.md", "a", encoding="utf-8") as f:
        f.write(line)

    print("✅ problems.md updated")
    return True
def read_all_problems():
    if not os.path.exists("problems.md"):
        return []
    rows = []
    with open("problems.md", "r") as f:
        for l in f:
            if l.startswith("| LC-"):
                rows.append(l.strip())
    return rows

# ---------- README ----------
def init_readme():
    if not os.path.exists("README.md"):
        print("⚠️ Create README manually first using provided template")
        exit()

def update_readme():
    init_readme()
    rows = read_all_problems()

    easy = sum(1 for r in rows if "| Easy |" in r)
    med  = sum(1 for r in rows if "| Medium |" in r)
    hard = sum(1 for r in rows if "| Hard |" in r)
    total = len(rows)

    recent = rows[-10:][::-1]

    recent_lines = []
    for r in recent:
        parts = [p.strip() for p in r.split('|')]
        title = parts[2]
        diff = parts[3]
        topic = parts[4]
        link = parts[-2]
        recent_lines.append(f"- {title} ({diff}, {topic}) → {link}")

    import re

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    new_content = re.sub(r"- Total: \d+", f"- Total: {total}", new_content)
    new_content = re.sub(r"- Easy: \d+", f"- Easy: {easy}", new_content)
    new_content = re.sub(r"- Medium: \d+", f"- Medium: {med}", new_content)
    new_content = re.sub(r"- Hard: \d+", f"- Hard: {hard}", new_content)

    new_content = re.sub(
        r"<!-- recent -->.*?---",
        "<!-- recent -->\n" + "\n".join(recent_lines) + "\n\n---",
        new_content,
        flags=re.S
    )

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ README updated")
    else:
        print("⚠️ README unchanged")
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
    print("🚀 Script started")
    print("ARGS:", sys.argv)
    if len(sys.argv) < 5:
        print("Usage: python create_problem.py <num> <slug> <topic> \"<title>\"")
        return

    num_raw, slug, topic, title = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    num = pad(num_raw)

    base = f"{topic}/LC-{num}-{slug}"
    link = f"https://leetcode.com/problems/{slug}/"

    diff = fetch_leetcode(slug)

    header = f"# LC-{num} {title}\n# {link}\n# Difficulty: {diff}\n\n"

    write(f"{base}/v1.py", header + "# v1\n\nclass Solution:\n    pass\n")
    write(f"{base}/v2.py", header + "# v2\n\nclass Solution:\n    pass\n")
    write(f"{base}/v3.py", header + "# v3\n\nclass Solution:\n    pass\n")

    write(f"{base}/notes.md", f"""# LC-{num} {title}

## Key Insight

## Mistake I made

## Pattern

## Trigger
(When should I think of this pattern again?)
""")

    append_problem(num, title, slug, topic, diff)
    update_readme()
    update_patterns(topic, num, title)

    print(f"Done → {base}")
    print("✅ Script executed successfully")
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Check a help article against the house voice and the publishing rules.

  python check_article.py <article.md>

Prints problems as "line N: message". Prints "Clean." when there are none.
Mechanical rules only; whether the article explains things well is for the writer.
"""
import os
import re
import sys

BANNED = [
    "simply", "just", "easily", "quickly", "obviously", "of course", "seamless", "seamlessly", "powerful",
    "robust", "intuitive", "effortless", "cutting-edge", "feel free", "might want to", "please", "kindly",
    "leverage", "utilize", "utilise", "functionality", "backend", "back-end", "payload", "endpoint",
    "e.g.", "i.e.", "etc.", "via", "merchant", "previously", "no longer",
]
VERBS = {
    "click": "select", "clicking": "selecting", "press": "select", "tick": "select", "untick": "clear",
    "enable": "turn on", "disable": "turn off", "navigate to": "go to", "log in": "sign in",
    "login": "sign in", "type in": "enter", "configure": "set up",
}
INTERNAL = [
    (r"\b(?:CP|CON|P20|SA|OC|FB|FAN|DEVOPS|SERV|OPS)-\d+\b", "ticket key"),
    (r"\b(?:Partner Portal|Firebase|Twilio|Spreedly|Hyperswitch|CloudPRNT)\b", "internal or vendor name"),
    (r"\b(?:FV2|V2|Phase \d)\b", "version label"),
    (r"(?i)\bselect \* from\b|\bstoreID\b|\bmerchantID\b", "internal identifier"),
    (r"(?i)\bcoming soon\b|\bin a future release\b|\broadmap\b", "roadmap talk"),
]
CONTRACTION = re.compile(r"\b(?:\w+n't|it's|that's|there's|you're|they're|we're|you'll|it'll|you've|we've|let's|can't|won't)\b", re.I)
MARKER = re.compile(r"\[(?:VERIFY|SCREENSHOT|TODO|TBD|CONFIRM)\b", re.I)
IMAGE = re.compile(r"!\[(.*?)\]\((.+?)\)")
BOLD = re.compile(r"\*\*.+?\*\*")


def check(path):
    problems = []
    base = os.path.dirname(os.path.abspath(path))
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    body_start = 0
    if lines and lines[0].strip() == "---":
        end = lines.index("---", 1)
        header = dict(l.split(":", 1) for l in lines[1:end] if ":" in l)
        for key in ("title", "slug", "category", "description", "tags"):
            if not header.get(key, "").strip():
                problems.append((1, f"header is missing '{key}'"))
        if len(header.get("title", "").strip()) > 60:
            problems.append((1, "title is over 60 characters"))
        if len(header.get("description", "").strip()) > 160:
            problems.append((1, "description is over 160 characters"))
        body_start = end + 1
    else:
        problems.append((1, "no metadata header"))

    in_callout = False
    for number, raw in enumerate(lines[body_start:], start=body_start + 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith(":::"):
            in_callout = not in_callout if line == ":::" or line.startswith(":::(") else in_callout
            continue
        if line.startswith("# "):
            problems.append((number, "remove the # heading; the help desk adds the title"))
        if MARKER.search(line):
            problems.append((number, "placeholder marker left in the article"))
        for match in IMAGE.finditer(line):
            if not match.group(1).strip():
                problems.append((number, "image has no alt text"))
            if not os.path.exists(os.path.join(base, match.group(2))):
                problems.append((number, f"image file not found: {match.group(2)}"))
        if IMAGE.search(line) or line.startswith("|") and set(line) <= set("|-: "):
            continue

        plain = BOLD.sub(" ", line)          # on-screen labels are exempt
        plain = re.sub(r'"[^"]*"', " ", plain)  # so are quoted messages
        low = plain.lower()
        for word in BANNED:
            if re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", low):
                problems.append((number, f"avoid '{word}'"))
        for word, better in VERBS.items():
            if re.search(r"\b" + re.escape(word) + r"\b", low):
                problems.append((number, f"use '{better}', not '{word}'"))
        if CONTRACTION.search(plain):
            problems.append((number, f"contraction: {CONTRACTION.search(plain).group(0)}"))
        if re.search(r"\bwe\b|\bour\b", low):
            problems.append((number, "'we' or 'our': name retailcloud, or address the reader as 'you'"))
        if "!" in plain.replace("![", ""):
            problems.append((number, "exclamation mark"))
        if "—" in plain or "–" in plain or re.search(r"\w - \w", plain) and not line.startswith("|"):
            problems.append((number, "dash joining clauses: use a full stop or a comma"))
        for pattern, label in INTERNAL:
            if re.search(pattern, line):
                problems.append((number, f"{label}: {re.search(pattern, line).group(0)}"))
        if not line.startswith(("|", "#")):
            for sentence in re.split(r"(?<=[.?])\s+", plain):
                if len(sentence.split()) > 32:
                    problems.append((number, f"sentence of {len(sentence.split())} words: split it"))
    return problems


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    problems = check(sys.argv[1])
    if not problems:
        print("Clean.")
        return
    for number, message in problems:
        print(f"line {number}: {message}")
    print(f"{len(problems)} to fix.")


if __name__ == "__main__":
    main()

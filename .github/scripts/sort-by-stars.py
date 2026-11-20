#!/usr/bin/env python3
"""Sort the entries of every README section by GitHub stars, most first.

An entry's repo is the one in its stars badge (img.shields.io/github/stars/<owner>/<repo>).
Entries without a badge keep their order at the end of their list. A blank line ends a
list, so groups split by blank lines are sorted on their own. "Contents" and "Official
Packages" are left as written.

Reads GITHUB_TOKEN from the environment (optional locally, set in CI). If any repo can't
be looked up, nothing is written and the script exits 1 listing the failures.

Usage: sort-by-stars.py [README.md]
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

KEEP_ORDER = {"## Contents", "## Official Packages"}
BADGE = re.compile(r"img\.shields\.io/github/stars/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def fetch_stars(repo, token):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "awesome-pocketbase-sort"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.load(resp)["stargazers_count"]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    token = os.environ.get("GITHUB_TOKEN", "")
    text = open(path, encoding="utf-8").read()

    repos = sorted({m.lower() for m in BADGE.findall(text)})
    print(f"looking up {len(repos)} repos", flush=True)
    stars, failed = {}, []
    for repo in repos:
        try:
            stars[repo] = fetch_stars(repo, token)
        except (urllib.error.URLError, TimeoutError, KeyError, ValueError) as e:
            failed.append(f"{repo}: {e}")
    if failed:
        print("could not look up:\n  " + "\n  ".join(failed), file=sys.stderr)
        return 1

    def key(line):
        m = BADGE.search(line)
        return -stars[m.group(1).lower()] if m else 1  # no badge: after every badged entry

    out, block, section = [], [], ""

    def flush():
        out.extend(block if section in KEEP_ORDER else sorted(block, key=key))  # stable sort
        block.clear()

    for line in text.split("\n"):
        if line.startswith("## "):
            flush()
            section = line.strip()
        if line.startswith("- "):
            block.append(line)
        else:
            flush()
            out.append(line)
    flush()

    new = "\n".join(out)
    if new == text:
        print("already sorted")
    else:
        open(path, "w", encoding="utf-8").write(new)
        print("re-sorted")
    return 0


if __name__ == "__main__":
    sys.exit(main())

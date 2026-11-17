#!/usr/bin/env bash
# Installs the skill for Claude Code on macOS, Linux or Git Bash.
set -e
here="$(cd "$(dirname "$0")" && pwd)"
dest="$HOME/.claude/skills/fanvista-help-articles"
mkdir -p "$HOME/.claude/skills"
rm -rf "$dest"
cp -r "$here/skills/fanvista-help-articles" "$dest"
python3 -m pip install --quiet -r "$here/requirements.txt" 2>/dev/null || python -m pip install --quiet -r "$here/requirements.txt"
echo "Installed to $dest. Restart Claude Code, then type /fanvista-help-articles."

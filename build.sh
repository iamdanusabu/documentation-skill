#!/usr/bin/env bash
# Rebuilds dist/help-desk-articles.skill (a zip of the skill folder) after any change.
set -e
cd "$(dirname "$0")"
python - <<'PY'
import os, zipfile
src = os.path.join("skills", "help-desk-articles")
out = os.path.join("dist", "help-desk-articles.skill")
os.makedirs("dist", exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f.endswith(".pyc"):
                continue
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, "skills"))
print("Built", out)
PY

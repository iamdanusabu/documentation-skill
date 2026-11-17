#!/usr/bin/env bash
# Rebuilds dist/fanvista-help-articles.skill (a zip of the skill folder) after any change.
set -e
cd "$(dirname "$0")"
python - <<'PY'
import os, zipfile
src = os.path.join("skills", "fanvista-help-articles")
out = os.path.join("dist", "fanvista-help-articles.skill")
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

# Installs the skill for Claude Code on Windows.
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$skills = Join-Path $HOME ".claude\skills"
$dest = Join-Path $skills "help-desk-articles"
New-Item -ItemType Directory -Force $skills | Out-Null
if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
Copy-Item -Recurse (Join-Path $here "skills\help-desk-articles") $dest
python -m pip install --quiet -r (Join-Path $here "requirements.txt")
Write-Host "Installed to $dest. Restart Claude Code, then type /help-desk-articles."

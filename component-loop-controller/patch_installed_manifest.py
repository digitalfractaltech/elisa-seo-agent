#!/usr/bin/env python3
import json, shutil, time
from pathlib import Path
p = Path.home() / '.openclaw' / 'skills' / 'manifest.json'
if not p.exists():
    print(f'No manifest found at {p}; skipping manifest patch.')
    raise SystemExit(0)
backup = p.with_name(f'manifest.json.backup-{int(time.time())}')
shutil.copy2(p, backup)
m = json.loads(p.read_text())
arr = m.setdefault('skills', [])
if 'loop-controller' not in arr:
    arr.append('loop-controller')
m['skill_count'] = len(arr)
p.write_text(json.dumps(m, indent=2))
print(f'Backed up manifest to {backup}')
print(f'skill_count={m["skill_count"]}')

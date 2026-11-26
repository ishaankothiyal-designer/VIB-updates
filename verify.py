"""Build and run current journey, fixture, resource and JavaScript checks."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    node = shutil.which('node')
    if not node:
        raise SystemExit('Node.js is needed for JavaScript validation. Install Node.js 22+ and retry.')
    commands = [
        [sys.executable, 'build_reports.py'],
        [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
        *[[sys.executable, script] for script in ['check.py','check-fixtures.py','check-all-reports.py']],
        [node, 'check-router.mjs'],
        *[[node,'--check',str(script.relative_to(ROOT))] for script in sorted((ROOT/'dist').glob('*.js'))],
    ]
    for command in commands:
        print('+', ' '.join(command), flush=True)
        subprocess.run(command, cwd=ROOT, check=True)
    print('PASS: all current checks. Browser/device checks remain separate.')

if __name__ == '__main__':
    main()

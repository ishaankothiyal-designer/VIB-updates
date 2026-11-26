"""Build and serve the preview locally. No cloud configuration or credentials needed."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=4336)
    args = parser.parse_args()
    subprocess.run([sys.executable, 'build_reports.py'], cwd=ROOT, check=True)
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT/'dist'))
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    except OSError as exc:
        parser.exit(1, f'Cannot start localhost:{args.port}: {exc}. Choose another port with --port 4337.\n')
    print(f'VIB preview: http://127.0.0.1:{args.port}/', flush=True)
    print('Press Ctrl+C to stop. Rebuild after source edits or restart this command.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped VIB preview.')
    finally:
        server.server_close()

if __name__ == '__main__':
    main()

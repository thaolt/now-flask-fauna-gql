from pathlib import Path
import sys

print((Path('..') / 'lib').resolve())

sys.path.append((Path('..') / 'lib').resolve())

from http.server import BaseHTTPRequestHandler
from datetime import datetime
import os
from supershop import *

load_env()


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    self.wfile.write(os.getenv("FAUNADB_API_KEY").encode())
    return


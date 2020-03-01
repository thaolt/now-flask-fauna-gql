from http.server import BaseHTTPRequestHandler
from os import getenv
from lib.supershop import *

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import json

load_env()

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

    self.wfile.write(
      '{"aaaa":"bbb"}'.encode()
    )

    return


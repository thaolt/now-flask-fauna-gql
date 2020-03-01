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

    client = Client(
      transport=RequestsHTTPTransport(
        url='https://graphql.fauna.com/graphql', 
        headers={'Authorization': 'Bearer ' + getenv("FAUNADB_SECRET")},
        use_json=True,
      ),
      fetch_schema_from_transport=True,
    )

    query = gql("""
    {
      findClientByID(id: "258719855966945812") {
        email
      }
    }
    """)

    self.wfile.write(
      json.dumps(client.execute(query)).encode('utf-8')
    )

    return


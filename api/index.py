from lib.app import app
from flask import Response
from lib.dbal import faunadb

@app.route('/hello')
def hello():
  return Response("<h1>Hello World!</h1>", minetype="text/html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return Response("<h1>Flask on ZEIT Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

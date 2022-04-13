from bottle import route, run
import sys
from helpers import hello


@route("/")
def index():
    texte = hello()
    return texte


run(host="0.0.0.0", port=sys.argv[1], reloader=True)

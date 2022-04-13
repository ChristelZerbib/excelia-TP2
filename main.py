from bottle import route, run
from helpers import hello


@route("/")
def index():
    texte = hello()
    return texte


run(host="localhost", port=8087)

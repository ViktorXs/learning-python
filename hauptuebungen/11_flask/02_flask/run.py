from flask import Flask

print("The app runs under the name: " + __name__)
app = Flask(__name__)  # Die Flask anwendung ist __name__ = app.py

@app.route("/")  # Ein "decorator".
def hello_world():  # Diese Funktion soll aufgerufen werden, wenn der Browser bei @app.route("/") das "/" aufruft.
    return "<p>Hello, World!</p>"

@app.route("/42")
def schwubbelduff():
    names = ("Viktor", "Vanessa")
    paragraph = "<p>Ein/e wilde/r " + names[1] + " betritt den Raum.</p>"

    return "<p>Oh, Hallo!</p>" + paragraph

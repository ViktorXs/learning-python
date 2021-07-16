from flask import Flask, render_template  # templates rendern um komplizierten Code nur ein mal zu haben?¿
app = Flask(__name__)


@app.route("/")
def locations():
    title = "Nice locations to visit"
    greeting = "Find your location of love!"
    places = ["Paris", "Stade", "Hamburg", "Praque"]

    return render_template("start.html", paragraph=greeting, location="Barcelona", locations=places, title=title)


@app.route("/test")
def good_toolse():
    greeting = "Testpage"
    return render_template("test.html", paragraph=greeting)

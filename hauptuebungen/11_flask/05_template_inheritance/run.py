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
    return render_template("locations.html", paragraph=greeting)


# @app.route("/platzhalter")
# def good_toolse():
#     greeting = "Welcome to the page of tools!"
#     sammelsurium = ["Dies", "Das", "Ananas", "Sowieso", "Aber", "Nein"]
#     return render_template("/platzhalter.html", paragraph=greeting, list=sammelsurium)

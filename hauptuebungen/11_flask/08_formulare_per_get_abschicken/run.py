from flask import Flask, render_template, request  # request modul notwendig, um URL Parameter zu übergeben
app = Flask(__name__)


@app.route("/")
def locations():
    title = "Nice locations to visit"
    greeting = "Find your location of love!"
    places = ["Paris", "Stade", "Hamburg", "Praque"]

    return render_template("start.html", paragraph=greeting, location="Barcelona", locations=places, title=title)


@app.route("/locations")
def test():
    parameters = request.args
    location = parameters.get("location")
    daytime = parameters.get("daytime")

    print(request.args)
    print("Location is set to: " + location)
    print("Preferred daytime is: " + daytime)

    return render_template("locations.html", location=location, daytime=daytime)

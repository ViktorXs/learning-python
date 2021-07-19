from flask import Flask, render_template, request  # request modul notwendig, um URL Parameter zu übergeben
app = Flask(__name__)


class Location():
    def __init__(self, location, duration):
        self.location = location
        self.duration = duration


@app.route("/")
def start():
    title = "Nice locations to visit"
    greeting = "Find your location of love!"

    places = [
        Location("Paris", 2),
        Location("Stade", 5),
        Location("Hamburg", 1),
        Location("Praque", 3)
    ]

#    places = [
#        {"location": "Paris", "duration": "4"},
#        {"location": "Stade", "duration": "10"},
#        {"location": "Hamburg", "duration": "2"},
#        {"location": "Praque", "duration": "6"},
#    ]
    return render_template("start.html",
                           paragraph=greeting,
                           location={"location": "Barcelona", "duration": 14},
                           locations=places,
                           title=title)


@app.route("/locations")
def locations():
    parameters = request.args
    location = parameters.get("location")
    daytime = parameters.get("daytime")
    days = parameters.get("days")

    return render_template("locations.html", location=location, daytime=daytime, days=days)

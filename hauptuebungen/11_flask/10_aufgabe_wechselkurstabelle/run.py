from flask import Flask, render_template, request
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


# Aufgabe ab hier
@app.route("/currency")
def calculator():

    # hochexperimentell
    parameters = request.args
    currency = parameters.get("currency")
    target = parameters.get("target")
    calculated = parameters.get("calculated")
    first_value = parameters.get("first_value")

    return render_template("currency.html",
                           currency=currency,
                           target=target,
                           first_value=first_value,
                           calulated=calculated)

# Schmierblatt:

    # 1 EUR = 1,95583 DEM
    # 1 DEM = 0,51129 EUR

    # dm_eur = 1.95583
    # usd_eur = 1.18
    # gbp_eur = 0.86
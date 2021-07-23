from flask import Flask, render_template, request

app = Flask(__name__)


class Location:
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
                           paraagraph=greeting,
                           location={"location": "Barcelona", "duration": 14},
                           locations=places,
                           title=title)


@app.route("/locations")
def locations():
    paraameters = request.args
    location = paraameters.get("location")
    daytime = paraameters.get("daytime")
    days = paraameters.get("days")

    return render_template("locations.html", location=location, daytime=daytime, days=days)


@app.route("/currency")
def dict_calculator():
    para = request.args
    curr1 = request.form.get("curr1", "EUR")
    curr2 = request.form.get("curr2", "USD")
    amount = float(para.get("amount", 1))
    calculated = para.get("calculated", 1)

    eur_to = {"DM": 1.95583, "USD": 1.17999, "GBP": 0.86000, "EUR": 1}
    dm_to = {"EUR": 0.51129, "USD": 0.60719, "GBP": 0.43927, "DM": 1}
    usd_to = {"EUR": 0.84746, "DM": 1.64693, "GBP": 0.73481, "USD": 1}
    gbp_to = {"EUR": 1.16279, "DM": 2.27652, "USD": 1.36090, "GBP": 1}

    if curr1 == "EUR" and curr2 in eur_to:
        calculated = amount * eur_to[curr2]
    elif curr1 == "DM" and curr2 in dm_to:
        calculated = amount * dm_to[curr2]
    elif curr1 == "USD" and curr2 in usd_to:
        calculated = amount * usd_to[curr2]
    elif curr1 == "GBP" and curr2 in gbp_to:
        calculated = amount * gbp_to[curr2]
    else:
        print("Currency currently not available.")

    return render_template("currency.html",
                           curr1=curr1,
                           curr2=curr2,
                           amount=amount,
                           calculated=calculated)

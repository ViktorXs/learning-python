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
    parameters = request.args
    currency = parameters.get("currency", "EUR")  # Kein NonteType TypeError mit zweitem Parameter, der mitgeladen wird.
    target = parameters.get("target", "USD")
    calculated = parameters.get("calculated", 1)
    amount = float(parameters.get("amount", 1))

#    eur_to = {
#        "DM": 1.95583,
#        "USD": 1.18,
#        "GBP": 0.86
#    }
#
#    for current in eur_to:
#        if currency == current:
#            print(current)
#            print(eur_to[current])

    # EUR
    if currency == "EUR" and target == "DM":
        calculated = amount * 1.95583
    if currency == "EUR" and target == "USD":
        calculated = amount * 1.18
    if currency == "EUR" and target == "GBP":
        calculated = amount * 0.86

    # DM
    if currency == "DM" and target == "EUR":
        calculated = amount * 0.51129
    if currency == "DM" and target == "USD":
        calculated = amount * 0.60719
    if currency == "DM" and target == "GBP":
        calculated = amount * 2.27652

    # USD
    if currency == "USD" and target == "EUR":
        calculated = amount * 0.84746
    if currency == "USD" and target == "DM":
        calculated = amount * 1.64693
    if currency == "USD" and target == "GBP":
        calculated = amount * 0.73481

    # GBP
    if currency == "GBP" and target == "EUR":
        calculated = amount * 1.16279
    if currency == "GBP" and target == "DM":
        calculated = amount * 0.43927
    if currency == "GBP" and target == "USD":
        calculated = amount * 1.36090

    return render_template("currency.html",
                           currency=currency,
                           target=target,
                           # amount=float(amount),
                           # calculated=round(calculated, 2))
                           amount=amount,
                           calculated=round(calculated, 2))

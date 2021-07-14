from flask import Flask, render_template  # templates rendern um komplizierten Code nur ein mal zu haben?¿
app = Flask(__name__)


@app.route("/")
def bad_tools():
    # Komplizierten Code, wie diesen:
    bad_tools = ["Screwdriver", "Hammer", "Cutter", "Duct tape"]
    output = ""

    for i in bad_tools:
        output += "<h3>" + i + "</h3>"

    return output


# Komplizierten Code in /template ausgelagert und als Vorlage vorbereitet
@app.route("/template")
def good_tools():
    tools = ["Duct tape", "Cutter", "Hammer", "Screwdriver"]
    title = "Tolle Sachen zum Demolieren von Sachen"

    return render_template("start.html", tool="Ruler", tools=tools, title=title)  # Man kann Parameter übergeben.
    # Links ist das, was in der start.html erwartet wird und rechts z.b. ein String oder Variable usw. aus dem Code.


# Übung muss sein
@app.route("/herr")
def herr():
    name = '"Reinsch"'
    frage = "Gibt's hier einen, der Herr " + name + " heißt?"
    title = "Moe's Bar, saufen bis zum Abwinken, was darfs denn sein?"
    return render_template("start.html", title=title, na_sowas=frage, herr=herr)

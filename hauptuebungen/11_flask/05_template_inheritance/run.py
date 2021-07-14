from flask import Flask, render_template  # templates rendern um komplizierten Code nur ein mal zu haben?¿
app = Flask(__name__)


@app.route("/")
def good_tools():
    tools = ["Duct tape", "Cutter", "Hammer", "Screwdriver"]
    title = "Tolle Sachen zum Demolieren von Sachen"

    return render_template("start.html", tool="Ruler", tools=tools, title=title)

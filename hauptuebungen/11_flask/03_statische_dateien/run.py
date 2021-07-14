from flask import Flask

print("The app runs under the name: " + __name__)
app = Flask(__name__)

@app.route("/")
def list_tools():
    # Auf folgender Weise eine HTML Seite aufbauen ist nicht praktisch und wird unübersichtlich.
    # Im nächsten Kapitel geht es um Templates um komplizierten Code zu verhindern:
    tools = ["Screwdriver", "Hammer", "Cutter", "Duct tape"]
    output = ""

    for i in tools:
        output += "<h3>" + i + "</h3>"

    return output

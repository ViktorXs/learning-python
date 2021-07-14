from flask import Flask

print("The app runs under the name: " + __name__)
app = Flask(__name__)

@app.route("/")
def list_tools():
    # Komplizierten Code, wie diesen verhindern:
    tools = ["Screwdriver", "Hammer", "Cutter", "Duct tape"]
    output = ""

    for i in tools:
        output += "<h3>" + i + "</h3>"

    return output

from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

REPORT_PATH = "../reports/report.json"


def load_report():
    if not os.path.exists(REPORT_PATH):
        return {}

    with open(REPORT_PATH, "r") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/report")
def report():
    data = load_report()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, redirect
from datetime import date
import os
import json

app = Flask(__name__)

DATA_FILE = "entries.json"

def load_entries():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_entries(entries):
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f)

@app.route("/", methods=["GET", "POST"])
def index():
    today = str(date.today())
    entries = load_entries()

    if request.method == "POST":
        entry_text = request.form["entry"]
        entries[today] = entry_text
        save_entries(entries)
        return redirect("/")

    entry_today = entries.get(today, None)
    return render_template("index.html", entry=entry_today, today=today)

app.run(host='0.0.0.0', port=10000)  # Wichtig: Port 10000 für Render

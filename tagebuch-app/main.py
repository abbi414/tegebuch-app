'''
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
'''

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            op = request.form.get("operation")
            if op == "add":
                result = num1 + num2
            elif op == "subtract":
                result = num1 - num2
            elif op == "multiply":
                result = num1 * num2
            elif op == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Division durch Null ist nicht erlaubt."
            else:
                error = "Ungültige Operation."
        except Exception as e:
            error = str(e)
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

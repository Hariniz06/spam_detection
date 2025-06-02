from flask import Flask, render_template, request
from pymongo import MongoClient
from utils.spam_rules import is_suspicious

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["spam_db"]
collection = db["spam_numbers"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    show_report = False
    phone = None

    if request.method == "POST":
        # Handle report action
        if "report_number" in request.form:
            reported_number = request.form["report_number"]
            collection.insert_one({"number": reported_number})
            result = f"{reported_number} has been reported as spam and added to the list!"
            return render_template("index.html", result=result)

        # Handle check action
        phone = request.form["phone"]
        spam_entry = collection.find_one({"number": phone})

        if spam_entry:
            result = f"⚠️ {phone} is a known spam number!"
        elif is_suspicious(phone):
            result = f"⚠️ {phone} looks suspicious based on rules!"
            show_report = True
        else:
            result = f"✅ {phone} seems safe."
            show_report = True

    return render_template("index.html", result=result, show_report=show_report, phone=phone)

if __name__ == "__main__":
    app.run(debug=True)

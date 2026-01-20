from flask import Flask, render_template, request
import pandas as pd
from topsis_logic import topsis
import re
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        weights = request.form.get("weights", "")
        impacts = request.form.get("impacts", "")
        email = request.form.get("email", "")

        # -------------------------------
        # BASIC VALIDATION
        # -------------------------------
        if not file or file.filename == "":
            return "No file uploaded"

        filename = file.filename.lower()

        if not (filename.endswith(".csv") or filename.endswith(".xlsx")):
            return "Please upload a CSV or XLSX file only"

        if not re.match(EMAIL_REGEX, email):
            return "Invalid email address"

        weights = weights.split(",")
        impacts = impacts.split(",")

        if len(weights) != len(impacts):
            return "Number of weights must equal number of impacts"

        for i in impacts:
            if i not in ["+", "-"]:
                return "Impacts must be either + or -"

        # -------------------------------
        # CHECK EMPTY FILE
        # -------------------------------
        file.seek(0, os.SEEK_END)
        if file.tell() == 0:
            return "Uploaded file is empty"
        file.seek(0)

        # -------------------------------
        # FILE READING (CSV or XLSX)
        # -------------------------------
        try:
            if filename.endswith(".xlsx"):
                df = pd.read_excel(file)
            else:
                try:
                    df = pd.read_csv(file, encoding="utf-8", sep=",")
                except Exception:
                    file.seek(0)
                    try:
                        df = pd.read_csv(file, encoding="latin1", sep=",")
                    except Exception:
                        file.seek(0)
                        df = pd.read_csv(file, encoding="latin1", sep=";")
        except Exception:
            return "Unable to read the file. Please check format."

        # -------------------------------
        # STRUCTURE VALIDATION
        # -------------------------------
        if df.shape[1] < 3:
            return "File must contain at least 3 columns (ID + criteria)"

        # -------------------------------
        # RUN TOPSIS
        # -------------------------------
        try:
            result = topsis(df, weights, impacts)
        except Exception:
            return "Error while computing TOPSIS. Ensure numeric values."

        output_file = "topsis_result.csv"
        result.to_csv(output_file, index=False)

        # -------------------------------
        # SEND EMAIL
        # -------------------------------
        try:
            send_email(email, output_file)
        except Exception:
            return "Failed to send email. Check email credentials."

        return "TOPSIS result sent successfully to your email!"

    return render_template("index.html")


def send_email(to_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "YOUR_EMAIL@gmail.com"
    msg["To"] = to_email
    msg.set_content("Attached is your TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="topsis_result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("aviralbhargava30@gmail.com", "misk xhzt rknh psyd")
        server.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True)

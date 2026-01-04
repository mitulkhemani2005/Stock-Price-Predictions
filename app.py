from flask import Flask, render_template, jsonify
import pandas as pd
import subprocess
import time
import re

app = Flask(__name__)

CSV_PATH = "data/stock_one_minute.csv"


# -------------------------
# Helper functions
# -------------------------

def get_current_price():
    try:
        df = pd.read_csv(CSV_PATH)
        if df.empty:
            return 0.0

        col = "Close" if "Close" in df.columns else df.columns[-1]
        return float(df.iloc[-1][col])

    except Exception as e:
        print("CSV Error:", e)
        return 0.0


def extract_float(text):
    """
    Extracts the LAST floating number from any string.
    Works for:
    - 123.45
    - [123.45]
    - [[123.45]]
    - tensor(123.45)
    """
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    return float(numbers[-1]) if numbers else 0.0


def get_predicted_price():
    try:
        result = subprocess.run(
            ["python", "predictmodel.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Prediction stderr:", result.stderr)
            return 0.0

        output = result.stdout.strip()
        return extract_float(output)

    except Exception as e:
        print("Prediction Exception:", e)
        return 0.0


# -------------------------
# Routes
# -------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train", methods=["POST"])
def train_model():
    try:
        subprocess.Popen(["python", "trainingmodel.py"])
        return jsonify({"status": "Training started"})
    except Exception as e:
        return jsonify({"status": "Training failed", "error": str(e)})


@app.route("/prices")
def prices():
    return jsonify({
        "current_price": get_current_price(),
        "predicted_price": get_predicted_price(),
        "timestamp": time.strftime("%H:%M:%S")
    })


if __name__ == "__main__":
    app.run(debug=True)

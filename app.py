from flask import Flask, jsonify, render_template
import pandas as pd
import time
import os
import threading
import re

from training.training import training_model
from predict.predict import predict_model

# -------------------------
# CONFIG
# -------------------------

DATA_PATH = "data/stock_long_data.csv"
SHORT_DATA_PATH = "data/stock_one_minute.csv"
MODEL_PATH = "model/model.keras"

STOCK = "TITAGARH.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10
EPOCHS = 50
LEARNING_RATE = 0.0025

CSV_PATH = SHORT_DATA_PATH

app = Flask(__name__)

# -------------------------
# HELPERS
# -------------------------

def get_current_price() -> float:
    try:
        df = pd.read_csv(CSV_PATH)
        if df.empty:
            return 0.0

        col = "Close" if "Close" in df.columns else df.columns[-1]
        return float(df.iloc[-1][col])

    except Exception as e:
        print("CSV Error:", e)
        return 0.0


def extract_float_from_string(text: str) -> float:
    """
    Extracts the LAST numeric value from any string.
    Handles:
    - '123.45'
    - '[123.45]'
    - 'tensor(123.45)'
    - 'Prediction: 123.45'
    """
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    return float(numbers[-1]) if numbers else 0.0


def _train_background():
    try:
        training_model(
            DATA_PATH,
            MODEL_PATH,
            STOCK,
            DAYS,
            INTERVAL,
            WINDOW_SIZE,
            EPOCHS,
            LEARNING_RATE
        )
        print("Training completed successfully")
    except Exception as e:
        print("Training failed:", e)


# -------------------------
# ROUTES
# -------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train", methods=["POST"])
def train():
    thread = threading.Thread(target=_train_background, daemon=True)
    thread.start()

    return jsonify({
        "status": "started",
        "message": "Model training started in background"
    })


@app.route("/prices")
def prices():
    try:
        raw_prediction = predict_model(
            STOCK,
            PREDICT_DAY,
            INTERVAL,
            WINDOW_SIZE,
            SHORT_DATA_PATH,
            MODEL_PATH
        )

        predicted_price = extract_float_from_string(str(raw_prediction))

    except Exception as e:
        print("Prediction error:", e)
        predicted_price = 0.0

    return jsonify({
        "current_price": get_current_price(),
        "predicted_price": predicted_price,
        "timestamp": time.strftime("%H:%M:%S")
    })


# -------------------------
# ENTRY POINT (RENDER)
# -------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
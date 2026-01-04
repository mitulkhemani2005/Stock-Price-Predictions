from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np

WINDOW_SIZE = 5
MODEL_PATH = "model/model.keras"

def create_model(WINDOW_SIZE, MODEL_PATH):
    model = Sequential()
    model.add(InputLayer((WINDOW_SIZE, 4)))
    model.add(LSTM(64))
    model.add(Dense(8, 'relu'))
    model.add(Dense(1, 'linear'))
    try:
        model.save(MODEL_PATH)
        print("Basic model created and saved successfully")
        return MODEL_PATH
    except:
        print("Error in saving the basic model")
        return False

def train_model(MODEL_PATH, X_input, y_input, epochs=50, learning_rate=0.001):
    model = load_model(MODEL_PATH)
    model.compile(loss=MeanSquaredError(), optimizer=Adam(learning_rate=learning_rate), metrics=[RootMeanSquaredError()])
    checkpoint = ModelCheckpoint(
        MODEL_PATH,
        monitor="loss",
        save_best_only=True,
        verbose=1
    )

    # ---------- SCALING ----------
    # X_input shape: (samples, 5, 4)
    n, t, f = X_input.shape

    scaler_X = MinMaxScaler()
    X_scaled = scaler_X.fit_transform(
        X_input.reshape(n * t, f)
    ).reshape(n, t, f)

    scaler_y = MinMaxScaler()
    y_scaled = scaler_y.fit_transform(
        y_input.reshape(-1, 1)
    )

    joblib.dump(scaler_X, "model/scaler_X.pkl")
    joblib.dump(scaler_y, "model/scaler_y.pkl")
    # -----------------------------


    model.fit(X_scaled, y_scaled, epochs=epochs, callbacks=[checkpoint])
    print("Model trained and saved successfully")
    return MODEL_PATH

def predict_next_minute_close(MODEL_PATH, X):
    model = load_model(MODEL_PATH)
    # ---------- SCALING ----------
    scaler_X = joblib.load("model/scaler_X.pkl")
    scaler_y = joblib.load("model/scaler_y.pkl")
    n, t, f = X.shape

    X_scaled = scaler_X.transform(
        X.reshape(n * t, f)
    ).reshape(n, t, f)

    pred_scaled = model.predict(X_scaled)
    # -----------------------------
    prediction = scaler_y.inverse_transform(pred_scaled)
    return prediction
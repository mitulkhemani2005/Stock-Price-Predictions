from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.metrics import RootMeanSquaredError
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model

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
    model.fit(X_input, y_input, epochs=epochs, callbacks=[checkpoint])
    print("Model trained and saved successfully")
    return MODEL_PATH

def predict_next_minute_close(MODEL_PATH, X):
    model = load_model(MODEL_PATH)
    prediction = model.predict(X)
    print("Prediction for next minute's closing price:", prediction)
    return prediction
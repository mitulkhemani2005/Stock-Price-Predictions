from training.training import training_model
from predict.predict import predict_model

DATA_PATH = "data/stock_long_data.csv"
SHORT_DATA_PATH = "data/stock_one_minute.csv"
MODEL_PATH = "model/model.keras"
STOCK = "GOLDBEES.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10
EPOCHS = 50
LEARNING_RATE = 0.0025

training_model(DATA_PATH, MODEL_PATH, STOCK, DAYS, INTERVAL, WINDOW_SIZE, EPOCHS, LEARNING_RATE)
predict_model(STOCK, PREDICT_DAY, INTERVAL, WINDOW_SIZE, SHORT_DATA_PATH, MODEL_PATH)
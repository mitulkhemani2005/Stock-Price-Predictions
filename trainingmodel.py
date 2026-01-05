from training.training import training_model

DATA_PATH = "data/stock_long_data.csv"
MODEL_PATH = "model/model.keras"
STOCK = "HDFCBANK.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10
EPOCHS = 50
LEARNING_RATE = 0.0025

training_model(DATA_PATH, MODEL_PATH, STOCK, DAYS, INTERVAL, WINDOW_SIZE, EPOCHS, LEARNING_RATE)
from predict.predict import predict_model

DATA_PATH = "data/stock_long_data.csv"
MODEL_PATH = "model/model.keras"
STOCK = "TITAGARH.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10

predict_model(STOCK, PREDICT_DAY, INTERVAL, WINDOW_SIZE, DATA_PATH, MODEL_PATH)
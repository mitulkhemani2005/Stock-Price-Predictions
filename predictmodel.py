from predict.predict import predict_model

DATA_PATH = "data/stock_one_minute.csv"
MODEL_PATH = "model/model.keras"
STOCK = "HDFCBANK.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10

predicted_price = predict_model(STOCK, PREDICT_DAY, INTERVAL, WINDOW_SIZE, DATA_PATH, MODEL_PATH)
print(predicted_price)
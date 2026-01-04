from training.training import training_model
from predict.predict import predict_model

DATA_PATH = "data/stock_long_data.csv"
MODEL_PATH = "model/model.keras"
STOCK = "TMCV.NS"
DAYS = "7d"
PREDICT_DAY = "1d"
INTERVAL = "1m"
WINDOW_SIZE = 10

training_model(DATA_PATH, MODEL_PATH, STOCK, DAYS, INTERVAL, WINDOW_SIZE)
predict_model(STOCK, PREDICT_DAY, INTERVAL, DATA_PATH, MODEL_PATH)
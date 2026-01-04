from data.fetch import fetch_long_term_data
from model.model import predict_next_minute_close
import numpy as np 
import pandas as pd

#PREDICTING THE NEXT MINUTE CLOSE PRICE USING THE LAST FETCHED DATASET
def predict_model(STOCK, DAYS, INTERVAL, DATA_PATH, MODEL_PATH):
    fetch_long_term_data(STOCK=STOCK, days=DAYS, interval=INTERVAL, DATA_PATH=DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    df = df.tail(1)
    High = float(df['High'].values[0])
    Low = float(df['Low'].values[0])
    Open = float(df['Open'].values[0])
    Volume = float(df['Volume'].values[0])
    input_data = np.array([[[Open, High, Low, Volume]]])
    Predicted_Value = predict_next_minute_close(MODEL_PATH, input_data)
    print("Predicted Next Minute Close Price: ", Predicted_Value[0][0])
    return Predicted_Value[0][0]
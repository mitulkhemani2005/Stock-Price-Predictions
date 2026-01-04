from data.fetch import fetch_long_term_data
from model.model import predict_next_minute_close
import numpy as np 
import pandas as pd
DATA_PATH = "data/stock_one_minute.csv"
STOCK = "TMCV.NS"
DAYS = "1d"
INTERVAL = "1m"

#FETCHING THE RECENT ONE DAY DATASET
fetch_long_term_data(STOCK=STOCK, days=DAYS, interval=INTERVAL, DATA_PATH=DATA_PATH)
df = pd.read_csv(DATA_PATH)
df = df.tail(1)
High = float(df['High'].values[0])
Low = float(df['Low'].values[0])
Open = float(df['Open'].values[0])
Volume = float(df['Volume'].values[0])
input_data = np.array([[[Open, High, Low, Volume]]])


#PREDICTING THE NEXT MINUTE CLOSE PRICE USING THE LAST FETCHED DATASET
predict_next_minute_close("model/model.keras", input_data)
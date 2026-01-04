import pandas as pd
import numpy as np

def create_sliding_windows(DATA_PATH, WINDOW_SIZE):
    df = pd.read_csv(DATA_PATH)
    feature_colm = ['High', 'Low', 'Open', 'Volume']
    target_colm = 'Close'
    X = []
    y = []
    for i in range(len(df) - WINDOW_SIZE):
        X.append(df[feature_colm].iloc[i:i+WINDOW_SIZE].values)
        y.append(df[target_colm].iloc[i+WINDOW_SIZE])
    if (X and y) == []:
        print ("Not enough data to create sliding windows. Please check the DATA_PATH or reduce the WINDOW_SIZE.")
        return np.array([]), np.array([])
    else:
        print(f"Created {len(X)} sliding windows each of size {WINDOW_SIZE}.")
        return np.array(X), np.array(y)
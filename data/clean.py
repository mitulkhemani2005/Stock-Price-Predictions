import pandas as pd

def clean_data(PATH):
    df = pd.read_csv(PATH)
    df = df.iloc[2:,:]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(PATH, index=False)
    return PATH
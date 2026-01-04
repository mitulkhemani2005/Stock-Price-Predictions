import pandas as pd

def clean_data(PATH):
    df = pd.read_csv(PATH)
    df = df.iloc[2:,:]
    df.reset_index(drop=True, inplace=True)
    df.rename(columns = {'Price': 'Date_Time'}, inplace=True)
    df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    df.sort_values('Date_Time', inplace=True)
    df.reset_index(drop = True, inplace=True)
    try:
        df.to_csv(PATH, index=False)
        print("Data cleaned and saved successfully")
        return True
    except:
        print("Error in saving the cleaned data")
        return False
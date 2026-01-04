import yfinance as yf

def fetch_long_term_data(STOCK = "NHPC.NS", days = "7d", interval = "1m", DATA_PATH = "data/stock_long_data.csv"):
    stock = yf.Ticker(STOCK)
    hist = yf.download(STOCK, period=days, interval=interval)
    try:
        hist.to_csv(DATA_PATH)
        print( "Fetched long term data successfully" )
        return True
    except:
        print("Error in saving the fetched long term data")
        return False
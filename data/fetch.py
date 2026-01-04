import yfinance as yf

def fetch_long_term_data(STOCK = "NHPC.NS", days = "7d"):
    stock = yf.Ticker(STOCK)
    hist = yf.download(STOCK, period=days, interval="1m")
    hist.to_csv("data/stock.csv")
    return "data/stock.csv"
from data.fetch import fetch_long_term_data
from data.clean import clean_data
DATA_PATH = fetch_long_term_data()
CLEANED_DATA_PATH = clean_data(DATA_PATH)
print(f"Data fetched and cleaned. Cleaned data path: {CLEANED_DATA_PATH}")
from data.fetch import fetch_long_term_data
from data.clean import clean_data
from data.window import create_sliding_windows
from model.model import create_model, train_model, predict_next_minute_close

def training_model (DATA_PATH, MODEL_PATH, STOCK, DAYS, INTERVAL, WINDOW_SIZE, EPOCHS, LEARNING_RATE):
    #FETCH AND CLEAN LONG TERM DATASET
    fetch_long_term_data(STOCK=STOCK, days=DAYS, interval=INTERVAL, DATA_PATH=DATA_PATH)
    clean_data(DATA_PATH)

    #CREATING SLINDING DATASET AS PER WINDOW SIZE
    X_input, y_input = create_sliding_windows(DATA_PATH, WINDOW_SIZE)

    #CREATING AND TRAINING THE MODEL
    create_model(WINDOW_SIZE, MODEL_PATH)
    train_model(MODEL_PATH, X_input, y_input, epochs=EPOCHS, learning_rate=LEARNING_RATE)

    print("Training Completed and Model Saved at ", MODEL_PATH)
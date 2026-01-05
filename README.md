# Stock Market Next Day Closing Predictions

**Project:** Predict next-day stock closing prices using historical time-series data and deep learning.

**Author:** Aspiring Data Scientist

## Table of Contents
- **About:** Project summary and goals
- **Repository Structure:** Key files and folders
- **Setup:** Install dependencies
- **Data:** Source and preprocessing
- **Training:** How to train the model
- **Prediction / Inference:** Run the model to predict next-day closing
- **Model:** Saved artifacts and code
- **Evaluation:** Metrics and how to reproduce results
- **Next Steps:** Ideas to improve the project
- **Contact:** How to reach me

## About
This project demonstrates a pipeline for predicting the next-day closing price of a stock using historical data and machine learning. It includes data fetching and cleaning, windowed time-series preparation, model training, and a simple prediction interface.

The goal is to explore time-series forecasting with practical tools and produce a reproducible workflow you can iterate on as you grow your data science skills.

## Repository Structure
- **app.py** — Application entry (serving/prediction interface)
- **run.py** — Alternative runner for the app (check which one your project uses)
- **trainingmodel.py** — Utilities for building/training the model
- **predictmodel.py** — Utilities for loading the model and running predictions
- **training/** — Training scripts (main training logic)
- **predict/** — Prediction scripts / CLI
- **data/** — Data fetching, cleaning and windowing helpers and CSVs
  - `stock_long_data.csv`, `stock_one_minute.csv` — example datasets
- **model/** — Trained model artifact (`model.keras`) and model helper code
- **templates/** — HTML templates for the app (e.g., `index.html`)

## Setup
1. Create a Python virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Inspect `requirements.txt` and install any additional packages if needed.

## Data
- Raw CSV files are in the `data/` folder.
- Preprocessing steps (see `data/clean.py` and `data/window.py`) typically include:
  - handling missing values
  - resampling or aggregating (if using high-frequency data)
  - feature engineering (returns, moving averages, volume features)
  - creating sliding windows / sequences for supervised learning

To fetch or refresh data, run the ingestion/fetch script in `data/` if provided.

## Training
Basic training steps:

```bash
# from repo root
python training/training.py
```

Notes:
- The training script will read prepared data from `data/`, build a model using code in `trainingmodel.py` / `model/`, and save the best model to `model/model.keras`.
- Check `training/training.py` for hyperparameters (sequence length, epochs, batch size, optimizer).

## Prediction / Inference
You can run the prediction script or use the app to get next-day closing predictions.

Command-line prediction (example):

```bash
python predict/predict.py
# or
python predictmodel.py
```

To run the web app (if implemented):

```bash
python run.py
# or
python app.py
```

The prediction utilities load `model/model.keras` by default — confirm paths in `predictmodel.py` / `predict/predict.py`.

## Model
- Model file: `model/model.keras`
- Model code and wrappers: `model/model.py`, `trainingmodel.py`, and `predictmodel.py`.

Tips:
- Version your model artifacts (e.g., include timestamped filenames) when experimenting.
- Save training logs (e.g., TensorBoard) to inspect learning curves.

## Evaluation
- Use appropriate regression/time-series metrics such as MAE, RMSE, MAPE.
- Evaluate on a hold-out test period that reflects the realistic forecasting horizon.
- Include baseline comparisons (e.g., naive persistence, moving average) to measure real gains.

## Next Steps / Improvements
- Add more features (technical indicators, macro variables, news sentiment).
- Try different model architectures (LSTM, GRU, Temporal Convolutional Networks, Transformers).
- Implement backtesting to simulate trading strategies using model outputs.
- Add CI to reproduce training and evaluation reliably.

## Contributing
Feel free to open issues or pull requests. Useful contributions include:
- improving data cleaning and feature engineering
- adding unit tests for data pipelines
- improving documentation and reproducibility

## License
Include a license of your choice (e.g., MIT) or specify terms here.

## Contact
If you'd like feedback or collaboration, reach out with your preferred contact details.

---

If you'd like, I can also:
- run the project to verify the app and training scripts
- add a minimal example notebook showing preprocessing → training → prediction
- create a requirements snapshot with exact package versions

Tell me which you'd like next.
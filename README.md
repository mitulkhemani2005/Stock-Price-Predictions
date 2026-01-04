# Stock Price Predictions

A machine learning project for predicting stock prices using deep learning techniques. This project implements LSTM (Long Short-Term Memory) neural networks to forecast stock market trends based on historical data.

## 📊 Overview

This project leverages historical stock market data to train predictive models that can forecast future stock prices on next minute. The implementation uses deep learning algorithms, specifically LSTM networks, which are well-suited for time series forecasting tasks due to their ability to capture long-term dependencies in sequential data.

## ✨ Features

- **Real-time Data Fetching**: Automatically retrieves historical stock data using financial APIs
- **Data Preprocessing**: Comprehensive data cleaning, normalization, and feature engineering
- **LSTM Model Training**: Deep learning model specifically designed for time series prediction
- **Price Forecasting**: Predicts future stock prices based on historical patterns
- **Model Evaluation**: Performance metrics including MSE, RMSE
- **Modular Architecture**: Clean separation of concerns with dedicated modules for data, training, and prediction

## 🏗️ Project Structure

```
Stock-Price-Predictions/
│
├── data/                   # Data storage and preprocessing scripts
│   ├── raw/               # Raw data files
│   └── processed/         # Processed data ready for training
│
├── model/                 # Trained model storage
│   └── saved_models/      # Serialized model files
│
├── predict/               # Prediction scripts and utilities
│   └── predictor.py       # Main prediction logic
│
├── training/              # Model training scripts
│   ├── train_model.py     # Training pipeline
│   └── model_config.py    # Model architecture and hyperparameters
│
├── run.py                 # Main execution script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mitulkhemani2005/Stock-Price-Predictions.git
   cd Stock-Price-Predictions
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Training and Prediction from the Model

```bash
python run.py
```

## 🔧 Configuration
- **Share Name**: Number of Market Share could be changed
- **LSTM layers**: Number and size of LSTM units
- **Dropout rate**: Regularization parameter
- **Learning rate**: Optimizer learning rate
- **Sequence length**: Number of historical days used for prediction

## 📊 Model Architecture

The project implements a deep LSTM neural network with the following architecture:

1. Input layer with sequence data
2. Multiple LSTM layers with dropout for regularization
3. Dense layers for feature extraction
4. Output layer for price prediction

## 📈 Performance Metrics

The model is evaluated using:

- **Mean Squared Error (MSE)**: Measures average squared difference
- **Root Mean Squared Error (RMSE)**: Square root of MSE for interpretability

## 📁 Data Sources

This project supports multiple data sources:

- **Yahoo Finance** (yfinance library)

## 🎯 Example Results

```
Stock: TITAGARH
RMSE: 0.0224
Loss: 5.02e-04


## 🛠️ Technologies Used

- **Python**: Core programming language
- **TensorFlow/Keras**: Deep learning framework
- **NumPy**: Numerical computations
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning utilities
- **yfinance**: Stock data retrieval

## ⚠️ Disclaimer

**This project is for educational and research purposes only.** 

Stock market prediction is inherently uncertain and involves significant risk. The predictions made by this model should not be used as the sole basis for investment decisions. Always conduct thorough research and consult with financial advisors before making investment choices.

Past performance does not guarantee future results.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mitul Khemani**
- GitHub: [@mitulkhemani2005](https://github.com/mitulkhemani2005)

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing libraries
- Financial data providers for making historical data accessible
- Research papers on LSTM applications in financial forecasting

## 📞 Contact

For questions or feedback, please open an issue on GitHub or reach out through the repository.

---

**Note**: Remember to star ⭐ this repository if you find it helpful!
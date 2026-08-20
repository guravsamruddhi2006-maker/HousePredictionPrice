# 🏠 House Price Prediction API

A machine-learning powered **California House Price Prediction API** built with **Python, FastAPI, Scikit-learn, Pandas, and Joblib**.

The project uses a **Random Forest Regressor** trained on the California Housing dataset to predict house prices based on geographical, demographic, and housing-related features.

## 🚀 Features

- 📊 California Housing dataset for model training
- 🌲 Random Forest Regression model
- ⚡ FastAPI REST API
- 🏠 Individual house price prediction
- 📁 CSV file-based batch predictions
- ✅ Request validation using Pydantic
- ❤️ Health-check endpoint
- 📥 CSV prediction results as downloadable files
- 💾 Trained model saved using Joblib
- 📦 Large model file managed using Git LFS

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| Scikit-learn | Machine learning |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Joblib | Model serialization |
| Pydantic | Request validation |
| Uvicorn | ASGI server |
| Git & Git LFS | Version control and large-file storage |

## 📂 Project Structure

```text
HousePricePredict/
├── train.py                 # Train and evaluate the ML model
├── response.py              # FastAPI application
├── house_model.joblib       # Trained Random Forest model
├── house_features.joblib    # List of model features
├── .gitignore               # Files ignored by Git
├── .gitattributes           # Git LFS configuration
└── README.md                # Project documentation
```

## 🧠 Machine Learning Model

The project uses the **California Housing dataset** provided by Scikit-learn.

### Model

```text
RandomForestRegressor
```

Configuration:

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

The dataset is divided into:

- **80%** training data
- **20%** testing data

The model is evaluated using:

- Mean Absolute Error (MAE)
- R² Score

The trained model is saved as:

```text
house_model.joblib
```

## 📋 Input Features

| Feature | Description |
|---|---|
| `MedInc` | Median income of the neighborhood |
| `HouseAge` | Average age of houses in the block |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Total population |
| `AveOccup` | Average number of occupants |
| `Latitude` | Latitude of the location |
| `Longitude` | Longitude of the location |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/guravsamruddhi2006-maker/HousePredictionPrice.git
cd HousePredictionPrice
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn pandas numpy scikit-learn joblib python-multipart
```

## ▶️ Running the Project

Start the FastAPI server with:

```bash
uvicorn response:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🔌 API Endpoints

### Home

```http
GET /
```

### Health Check

```http
GET /health
```

### Predict House Price

```http
POST /predict
```

Example request:

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984,
  "AveBedrms": 1.024,
  "Population": 322,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

### CSV Batch Prediction

```http
POST /predict-file
```

The endpoint accepts a `.csv` file containing all eight required features and returns a downloadable CSV with predictions.

## 🔄 How It Works

```text
California Housing Dataset
          ↓
     Data Preparation
          ↓
   Train/Test Split
          ↓
 Random Forest Regressor
          ↓
    Model Evaluation
          ↓
    Save Model (.joblib)
          ↓
      FastAPI Server
          ↓
 ┌────────┴─────────┐
 ↓                  ↓
JSON Prediction   CSV Prediction
 ↓                  ↓
Predicted Price   Downloadable CSV
```

## 💾 Git LFS

The trained `house_model.joblib` file is large, so this project uses **Git Large File Storage (Git LFS)**.

Install and initialize Git LFS:

```bash
git lfs install
```

Then clone the repository normally:

```bash
git clone https://github.com/guravsamruddhi2006-maker/HousePredictionPrice.git
```

## 🔮 Future Improvements

- Add a web-based frontend
- Deploy the API to a cloud platform
- Add authentication and authorization
- Add model versioning
- Improve model performance through hyperparameter tuning
- Add visualization of prediction results
- Add automated testing
- Add Docker support
- Add CI/CD using GitHub Actions

## 👩‍💻 Author

**Samruddhi Gurav**

GitHub: https://github.com/guravsamruddhi2006-maker

## 📜 License

This project is intended for educational and portfolio purposes.

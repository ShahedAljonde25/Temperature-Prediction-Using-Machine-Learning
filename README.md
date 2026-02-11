# Machine Learning Temperature Forecasting

This project predicts **average daily temperature** using real-world climate data and machine learning.
It demonstrates a complete data science workflow: data cleaning, feature engineering, exploratory
data analysis, and regression modeling.

---

## Project Overview

Traditional weather forecasting relies on complex physical models that are computationally expensive
and unstable in the long term. This project applies **machine learning** as a data-driven alternative
to predict average temperature using historical climate variables.

The dataset spans **25 years (2000–2025)** and is collected from **NOAA – JFK Airport, New York**.

---

## Dataset

- **Source:** NOAA – National Centers for Environmental Information
- **Location:** JFK Airport, New York
- **Records:** 9,430 daily observations
- **Time Range:** 2000–2025

### Features
- Average wind speed (AWND)
- Precipitation (PRCP)
- Snowfall (SNOW)
- Snow depth (SNWD)
- Maximum temperature (TMAX)
- Minimum temperature (TMIN)
- Wind direction (WDF5)
- Wind speed (WSF5)

### Engineered Features
- Wind U-component
- Wind V-component

### Target
- **Average Temperature (TAVG)**

---

## Data Cleaning and Preprocessing

- Removed columns with excessive missing values (TSUN)
- Handled missing values using **Day-of-Year seasonal imputation**
- Converted date column to `datetime`
- Standardized temperature units (Fahrenheit → Celsius)
- Converted wind direction from degrees to vector form using sine and cosine
- Removed duplicates and inconsistent values

---

## Exploratory Data Analysis

- Correlation analysis between climate variables
- Distribution analysis of numerical features
- Relationship analysis between snow depth and temperature
- Wind speed trends over time
- Outlier detection using **DBSCAN**

---

## Machine Learning Models

- Random Forest Regression
- Support Vector Regression (SVR)
- **XGBoost Regression**

### Evaluation Metrics
- RMSE
- MAE
- R² Score

---

## Results

| Model | RMSE | MAE | R² |
|------|------|------|----|
| Random Forest | 4.30 | 3.09 | 0.93 |
| SVR | 3.80 | 2.35 | 0.95 |
| **XGBoost** | **3.52** | **2.32** | **0.95** |

## Conclusion

After thorough data preprocessing and analysis, the dataset became clean, consistent, and suitable
for machine learning. Among the tested models, XGBoost showed superior performance, making it the
most effective choice for average temperature prediction in this project.

---

## Author

**Shahed Mohannad Aljundi**  
Machine Learning & Data Science Student

---

## License

This project is intended for academic and educational purposes.


**XGBoost achieved the best performance** with the lowest error and highest accuracy.

Model Deployment with FastAPI

To make the model accessible and usable in real-time applications, the best-performing model (XGBoost) was deployed using FastAPI.

FastAPI allows us to:

Build a high-performance REST API

Send climate data as JSON input

Receive temperature predictions instantly

Integrate the model into web or mobile applications

📌 API Endpoint
POST /weather_predict

This endpoint accepts climate variables in JSON format and returns the predicted average temperature.

Example Request (JSON)
{
  "AWND": 5.2,
  "PGTM": 1200,
  "PRCP": 0.0,
  "SNOW": 0.0,
  "SNWD": 0.0,
  "TMAX": 28.5,
  "TMIN": 20.1,
  "WDF5": 180,
  "WSF5": 12.0,
  "U_Component": -5.6,
  "V_Component": 0.0
}

Example Response
{
  "predicted_temperature": 24.3
}

🛠 How to Run the API Locally
1️⃣ Install Dependencies
pip install fastapi uvicorn xgboost scikit-learn numpy pandas

2️⃣ Run the Server
uvicorn weather_modiling:app --reload

3️⃣ Open Interactive Docs
http://127.0.0.1:8000/docs


FastAPI automatically generates interactive API documentation.

🏗 Project Structure
weather_prediction/
│
├── weather_modiling.py
├── weather_prediction.sav
├── dataset.csv
└── README.md



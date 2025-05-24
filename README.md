# 🚗 Car Price Predictor

This project is a **Machine Learning-powered web application** that predicts the resale price of a used car based on key features like brand, model, fuel type, year, and kilometers driven.

It is built with **Flask**, trained using **Linear Regression**, and deployed using **Render.com**.

> 🔗 **Live App**: [https://car-price-predictor-with-linear.onrender.com/](https://car-price-predictor-with-linear.onrender.com/)

---

## 📊 Features

- Predicts car resale prices instantly
- Built using a cleaned real-world dataset
- Dynamic form: selects brand, model, year, fuel type, and mileage
- Fully responsive UI with Bootstrap 4
- Trained Linear Regression model with optimized pipeline
- Deployed using Gunicorn on Render.com

---

## 🧠 Machine Learning Overview

### Dataset Preprocessing

- Removed rows with missing or non-numeric data in `year`, `kms_driven`, and `price`
- Cleaned `kms_driven` by removing commas and units
- Removed `Ask For Price` values in `Price`
- Trimmed car names to first 3 words for consistency
- Removed outliers above ₹60 lakh
- Final dataset saved as: `cleaned_car_dataset.csv`

### Model Pipeline

- Input Features: `name`, `company`, `year`, `kms_driven`, `fuel_type`
- Target: `Price`
- One-hot encoding for categorical features using `make_column_transformer`
- Trained with `LinearRegression`
- Cross-validated R² scores over 1000 random seeds
- Final model pickled as `LinearRegressionModel.pkl`

---

## 🌐 Deployment

Hosted on **Render.com**.

### Render Settings:

- **Build command**: `pip install -r requirements.txt`
- **Start command**: `gunicorn app:app`
- **Runtime**: Python 3.11

### requirements.txt:

Flask==2.2.5
flask-cors==3.0.10
scikit-learn==1.2.2
pandas==1.5.3
numpy==1.24.3
gunicorn==20.1.0

---

## 🙌 Author

Built and maintained by Asad Ishteaque.

Contributions, issues, and suggestions are welcome!

## 📝 License

This project is open-sourced under the MIT License.

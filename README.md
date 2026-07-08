# Crop Prediction System 🌱

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)

A Machine Learning based web application that recommends the best crop to grow based on various soil nutrients and parameters. 

**Live Demo:** [https://crop-p.onrender.com](https://crop-p.onrender.com)

## 📖 Overview
This project utilizes a **Logistic Regression** model trained on agricultural data to predict the most suitable crop for a given soil environment. It takes 11 critical soil and environmental parameters as input and provides an instant crop recommendation (such as grapes, mango, mulberry, pomegranate, potato, or ragi) to help optimize agricultural yield.

## 🚀 Features
* **Interactive Web Interface:** A clean, user-friendly form to input soil data.
* **Real-Time Predictions:** Instant crop recommendation upon form submission.
* **11 Input Parameters Supported:**
  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * pH level
  * Electrical Conductivity (EC)
  * Sulphur (S)
  * Copper (Cu)
  * Iron (Fe)
  * Manganese (Mn)
  * Zinc (Zn)
  * Boron (B)

## 🛠️ Technologies Used
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, Joblib (for model persistence)
* **Frontend:** HTML, CSS

## 📁 Project Structure
```text
├── app.py                  # Main Flask application file
├── crop_prediction.py      # Data preprocessing and model training script
├── crop_model.joblib       # Pre-trained Logistic Regression model
├── requirements.txt        # Python dependencies
└── templates/
    ├── index.html          # Main UI for the prediction form
    └── about.html          # About the developer page

```

## 💻 Local Installation & Setup

To run this project locally on your machine, follow these steps:

1. **Clone the repository** (or download the files):
```bash
git clone <your-repository-url>
cd <your-repository-directory>

```


2. **Install the required dependencies:**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt

```


3. **Run the Flask application:**
```bash
python app.py

```


4. **Access the web app:**
Open your browser and navigate to `http://localhost:5000` (or `http://0.0.0.0:5000`).

## 🧠 Model Training Details

The machine learning model was built using `scikit-learn`'s `LogisticRegression`. The dataset is loaded from a remote CSV, split into an 80/20 train-test ratio, and evaluated using standard classification metrics (accuracy score, confusion matrix, and classification report). The trained model is then serialized into `crop_model.joblib` for rapid inference in the web app.


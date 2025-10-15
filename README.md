# ❤️ Predicting Heart Problems Using LRA (Logistic Regression Algorithm)

This project uses the **Logistic Regression Algorithm (LRA)** to predict the likelihood of heart disease in patients based on various medical attributes. The aim is to assist in early detection and provide actionable insights using data science.

https://web-production-99b87.up.railway.app/

https://dineshkonala.github.io/Predicting-Heart-Problems-Using-LRA/
---

## 📊 Project Overview

### Objective:
To build a **binary classification model** that predicts whether a person is likely to have heart disease or not, using **Logistic Regression**, a popular supervised machine learning algorithm.

### Dataset:
- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- **Format:** CSV
- **Features Include:**
  - Age
  - Sex
  - Chest pain type (cp)
  - Resting blood pressure (trestbps)
  - Cholesterol level (chol)
  - Fasting blood sugar (fbs)
  - Maximum heart rate (thalach)
  - and more...

---

## 📂 Project Structure

```bash
Predicting-Heart-Problems-Using-LRA/
├── data_set/
│   └── heart.csv
├── notebook/
│   └── heart_disease_prediction.ipynb
├── src/
│   └── model.py
├── images/
│   └── output_graphs.png
├── requirements.txt
└── README.md



## to install this project on linux

sudo apt update
sudo apt install python3 python3-pip python3-venv git -y

git clone https://github.com/DINESHKONALA/Predicting-Heart-Problems-Using-LRA.git
cd Predicting-Heart-Problems-Using-LRA

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver 0.0.0.0:8000



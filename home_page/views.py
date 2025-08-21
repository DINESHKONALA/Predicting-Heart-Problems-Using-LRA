from django.shortcuts import render
import joblib
import numpy as np
import os
# from  ark_elior.home_page.form_ import HeartForm
from .form import HeartForm
from django.conf import settings

# Load model and scaler
# MODEL_PATH = os.path.join(r"ark_elior\home_page\models\heart_model.pkl")
# SCALER_PATH = os.path.join(r"ark_elior\home_page\models\scaler.pkl")

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("home_page\ml\models")))
# model = joblib.load(os.path.join(BASE_DIR, "heart_model.pkl"))
# scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

# model = joblib.load(MODEL_PATH)
# scaler = joblib.load(SCALER_PATH)

model_path = os.path.join(settings.BASE_DIR, "home_page", "models", "heart_model.pkl")
model = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, "home_page", "models", "scaler.pkl")
scaler=joblib.load(scaler_path)

def predict_heart(request):
    result = None
    if request.method == "POST":
        form = HeartForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            data = np.array(data).reshape(1, -1)
            data = scaler.transform(data)
            prediction = model.predict(data)[0]
            result = "High risk of Heart Disease" if prediction == 1 else "Low risk"
    else:
        form = HeartForm()
    return render(request, "index.html", {"form": form, "result": result})

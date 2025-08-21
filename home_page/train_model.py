# train_model.py
import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# ---- STEP 1: Load dataset ----
# replace with your dataset path
df = pd.read_csv("ark_elior\home_page\Heart_disease_cleveland_new.csv")

# Features & target
X = df.drop("target", axis=1)   # "target" column is 1 = disease, 0 = healthy
y = df["target"]

# ---- STEP 2: Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- STEP 3: Scale ----
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---- STEP 4: Train model ----
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ---- STEP 5: Evaluate ----
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---- STEP 6: Save model & scaler ----
# joblib.dump(model, "heart_model.pkl")
# joblib.dump(scaler, "scaler.pkl")


# Get the current directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create a "models" folder inside your Django app
models_dir = os.path.join(BASE_DIR, "models")
os.makedirs(models_dir, exist_ok=True)

# Save files there
joblib.dump(model, os.path.join(models_dir, "heart_model.pkl"))
joblib.dump(scaler, os.path.join(models_dir, "scaler.pkl"))

print("✅ Model and scaler saved!")

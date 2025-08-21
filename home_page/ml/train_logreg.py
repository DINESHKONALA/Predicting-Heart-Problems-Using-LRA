import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import os

# Load dataset (UCI heart dataset format)
df = pd.read_csv("ark_elior\home_page\ml\Heart_disease_cleveland_new.csv")  
X = df.drop("target", axis=1)
y = df["target"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train LRA model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model + scaler
# Get the current directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create a "models" folder inside your Django app
models_dir = os.path.join(BASE_DIR, "models")
os.makedirs(models_dir, exist_ok=True)

# Save files there
joblib.dump(model, os.path.join(models_dir, "heart_model.pkl"))
joblib.dump(scaler, os.path.join(models_dir, "scaler.pkl"))

print("✅ Model & Scaler saved!")

from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField(label="Sex (male=1, female=0)")
    cp = forms.IntegerField(label="Chest Pain Type")
    trestbps = forms.IntegerField(label="Resting Blood Pressure")
    chol = forms.IntegerField(label="Cholesterol")
    fbs = forms.IntegerField(label="Fasting Blood Sugar > 120 (1=yes,0=no)")
    restecg = forms.IntegerField(label="Resting ECG")
    thalach = forms.IntegerField(label="Max Heart Rate Achieved")
    exang = forms.IntegerField(label="Exercise Induced Angina (1=yes,0=no)")
    oldpeak = forms.FloatField(label="ST Depression")
    slope = forms.IntegerField(label="Slope of ST Segment")
    ca = forms.IntegerField(label="Number of Major Vessels (0-3)")
    thal = forms.IntegerField(label="Thalassemia (1=normal, 2=fixed defect, 3=reversible)")

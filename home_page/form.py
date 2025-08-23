from django import forms

class HeartForm(forms.Form):
    GENDER_CHOICES = [
        (1, 'Male'),
        (0, 'Female'),
    ]
    sex = forms.TypedChoiceField(
    choices=GENDER_CHOICES,
    widget=forms.RadioSelect,
    coerce=int,  # Converts string → int automatically
    label="Gender"
    )

    AGE_CHOICES = [("", "Select Age")] + [(i, i) for i in range(1, 201)]
    age = forms.TypedChoiceField(
    choices=AGE_CHOICES,
    coerce=int,
    label="Age"
    )

    # sex = forms.IntegerField(label="Sex (male=1, female=0)")

    CP_CHOICES = [
        (0, "Typical Angina"),
        (1, "Atypical Angina"),
        (2, "Non-anginal Pain"),
        (3, "Asymptomatic"),
    ]
    cp = forms.TypedChoiceField(
        choices=CP_CHOICES,
        coerce=int,
        label="Chest Pain Type"
    )

    TRESTBPS_CHOICES = [(i, i) for i in range(50, 251)]
    trestbps = forms.TypedChoiceField(
    choices=TRESTBPS_CHOICES,
    coerce=int,
    label="Resting Blood Pressure"
    )

    CHOL_CHOICES = [(i, i) for i in range(100, 601)]
    chol = forms.TypedChoiceField(
    choices=CHOL_CHOICES,
    coerce=int,
    label="Cholesterol"
    )

    # Fasting Blood Sugar
    FBS_CHOICES = [(1, "Yes (>120 mg/dl)"), (0, "No")]
    fbs = forms.TypedChoiceField(
        choices=FBS_CHOICES,
        coerce=int,
        widget=forms.RadioSelect,
        label="Fasting Blood Sugar > 120"
    )

    # Resting ECG
    RESTECG_CHOICES = [
        (0, "Normal"),
        (1, "ST-T Wave Abnormality"),
        (2, "Left Ventricular Hypertrophy"),
    ]
    restecg = forms.TypedChoiceField(
        choices=RESTECG_CHOICES,
        coerce=int,
        label="Resting ECG"
    )

    THALACH_CHOICES = [(i, i) for i in range(50, 251)]
    thalach = forms.TypedChoiceField(
    choices=THALACH_CHOICES,
    coerce=int,
    label="Max Heart Rate Achieved"
    )
    # Exercise Induced Angina
    EXANG_CHOICES = [(1, "Yes"), (0, "No")]
    exang = forms.TypedChoiceField(
        choices=EXANG_CHOICES,
        coerce=int,
        widget=forms.RadioSelect,
        label="Exercise Induced Angina"
    )

    OLDPEAK_CHOICES = [(round(i * 0.1, 1), round(i * 0.1, 1)) for i in range(0, 101)]
    oldpeak = forms.TypedChoiceField(
    choices=OLDPEAK_CHOICES,
    coerce=float,
    label="ST Depression"
    )
    # Slope of ST Segment
    SLOPE_CHOICES = [
        (0, "Upsloping"),
        (1, "Flat"),
        (2, "Downsloping"),
    ]
    slope = forms.TypedChoiceField(
        choices=SLOPE_CHOICES,
        coerce=int,
        label="Slope of ST Segment"
    )

    CA_CHOICES = [(i, i) for i in range(0, 4)]
    ca = forms.TypedChoiceField(
    choices=CA_CHOICES,
    coerce=int,
    label="Number of Major Vessels (0–3)"
    )
    # Thalassemia
    THAL_CHOICES = [
        (1, "Normal"),
        (2, "Fixed Defect"),
        (3, "Reversible Defect"),
    ]
    thal = forms.TypedChoiceField(
        choices=THAL_CHOICES,
        coerce=int,
        label="Thalassemia"
    )    
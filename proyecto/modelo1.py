import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load your adapted data
df = pd.read_csv('datos_sospechosos.csv')

# 2. Split into features (X) and target (y)
feature_cols = [
    'Edad',
    'ArrestosPrevios',
    'FaltasTrabajo',
    'NivelEducacion',
    'Multas',
    'AntecedentesFamiliares',
    'HorasFueraCasa'
]
X = df[feature_cols]
y = df['Sospechoso']

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# 5. Train a basic classifier
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# 6. Evaluate on the test set
y_pred = model.predict(X_test_scaled)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Sospechoso', 'Sospechoso']))

# 7. Function to predict on new observations
def predict_person(obs_dict):
    """
    obs_dict example:
    {
        'Edad': 29,
        'ArrestosPrevios': 1,
        'FaltasTrabajo': 4,
        'NivelEducacion': 14,
        'Multas': 2,
        'AntecedentesFamiliares': 1,
        'HorasFueraCasa': 6
    }
    Returns: 'Sospechoso' or 'No Sospechoso'
    """
    obs_df = pd.DataFrame([obs_dict])
    obs_scaled = scaler.transform(obs_df[feature_cols])
    pred = model.predict(obs_scaled)[0]
    return 'Sospechoso' if pred == 1 else 'No Sospechoso'

# Example usage:
new_person = {
    'Edad': 33,
    'ArrestosPrevios': 0,
    'FaltasTrabajo': 1,
    'NivelEducacion': 16,
    'Multas': 0,
    'AntecedentesFamiliares': 0,
    'HorasFueraCasa': 2
}
result = predict_person(new_person)
print(f"\nNew observation predicted as: {result}")

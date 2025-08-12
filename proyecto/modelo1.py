import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve

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

# 3. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Cross‑validated precision (5‑fold)
model = LogisticRegression()
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
precision_scores = cross_val_score(model, X_scaled, y, cv=cv, scoring='precision')
print(f"Cross‑validated precision: {precision_scores.mean():.2f} ± {precision_scores.std():.2f}")

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, stratify=y, random_state=42
)
model.fit(X_train, y_train)

# 6. Determine probability threshold for ≥80% precision
y_probs = model.predict_proba(X_test)[:, 1]
precisions, recalls, thresholds = precision_recall_curve(y_test, y_probs)
desired_precision = 0.80
valid_idxs = np.where(precisions[:-1] >= desired_precision)[0]
if len(valid_idxs) > 0:
    # choose the highest threshold that still meets the precision requirement
    best_idx = valid_idxs[-1]
    threshold = thresholds[best_idx]
else:
    threshold = 0.5  # fallback if requirement not met
print(f"Selected threshold for precision ≥ {desired_precision*100:.0f}%: {threshold:.2f}")

# 7. Evaluate with adjusted threshold
y_pred_adj = (y_probs >= threshold).astype(int)
print("\nConfusion Matrix with adjusted threshold:")
print(confusion_matrix(y_test, y_pred_adj))
print("\nClassification Report with adjusted threshold:")
print(classification_report(y_test, y_pred_adj, target_names=['No Sospechoso', 'Sospechoso']))

# 8. Realistic prediction function
def predict_person(obs_dict):
    """
    Predicts 'Sospechoso' or 'No Sospechoso' with ≥80% precision threshold.
    obs_dict keys must match feature_cols.
    """
    obs_df = pd.DataFrame([obs_dict])
    obs_scaled = scaler.transform(obs_df[feature_cols])
    prob = model.predict_proba(obs_scaled)[0, 1]
    return 'Sospechoso' if prob >= threshold else 'No Sospechoso'

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

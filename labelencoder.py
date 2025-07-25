# -------SCALING
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Step 1: Sample Data
data = pd.DataFrame({
    'Age': [20, 25, 30, 35],
    'Income': [30000, 50000, 80000, 100000]
})

# Step 2: Initialize the Scaler
scaler = StandardScaler()

# Step 3: Combine Fitting and Scaling (optional)
scaled_data = scaler.fit_transform(data)

# Step 6: View Scaled Data
scaled_df = pd.DataFrame(scaled_data, columns=data.columns)
print(scaled_df)

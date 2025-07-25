# Step 1: Import libraries
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Step 2: Create dataset
# Features: [Weight (grams), Size (cm)]
X = np.array([
    [150, 7],  # Apple
    [140, 6],  # Apple
    [160, 7],  # Apple
    [200, 9],  # Orange
    [210, 10], # Orange
    [220, 10]  # Orange
])

# Labels: Apple or Orange
y = np.array(['Apple', 'Apple', 'Apple', 'Orange', 'Orange', 'Orange'])

# Step 3: Divide data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Step 4: Use the Scikit-learn implementation of the classifier
K = 3
model = KNeighborsClassifier(n_neighbors=K)
model.fit(X_train, y_train)  # Train the model

# Step 5: Predict test set
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
score = model.score(X_test, y_test)

print("Test data predictions:", y_pred)
print("Actual labels:", y_test)
print("Accuracy (accuracy_score):", accuracy)
print("Score (model.score):", score)

# Prediction - Predict a new fruit
new_fruit = [[160, 8]]  # A fruit with weight 160g and size 8 cm
prediction = model.predict(new_fruit)
print("Predicted fruit for [160,8]:", prediction[0])

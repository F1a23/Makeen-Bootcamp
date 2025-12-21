# ============================================
# 0) Import Libraries
# ============================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ============================================
# 1) Data Collection - Read Excel file
# ============================================
# Make sure the file is in the same folder, or use full path
df = pd.read_excel("simple linear regressoin data.xlsx")

print("===== First 5 rows of data =====")
print(df.head())
print("\nData shape (rows, columns):", df.shape)

# ============================================
# 2) Data Cleaning / Preprocessing
#    - Check missing values
#    - Basic statistics
# ============================================
print("\n===== Missing values in each column =====")
print(df.isnull().sum())

print("\n===== Basic statistics of the data =====")
print(df.describe())

#need to clean if it has Missing values:
# you would handle them (drop or fill).
# But in your case, both columns have 0 missing values.

# ============================================
# 3) Define Features (X) and Target (y)
#    - X: hours_studied
#    - y: exam_score
# ============================================
X = df[["hours_studied"]]     # Feature(s)
y = df["exam_score"]          # Target

# ============================================
# 4) Train/Test Split
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% test, 80% train
    random_state=42
)

print("\nTrain shape:", X_train.shape)
print("Test shape:", X_test.shape)

# ============================================
# 5) Choose and Train the Model (Linear Regression)
# ============================================
model = LinearRegression()

# This is the training step in ML workflow
model.fit(X_train, y_train)

# Show learned parameters (slope and intercept)
print("\n===== Model Parameters =====")
print("Slope (coefficient m):", model.coef_[0])
print("Intercept (b):", model.intercept_)
print(f"Equation: exam_score = {model.coef_[0]:.4f} * hours_studied + {model.intercept_:.4f}")

# ============================================
# 6) Testing & Evaluation
#    - Predict on test data
#    - Calculate MAE, MSE, RMSE, R2
# ============================================
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n===== Evaluation Metrics =====")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# ============================================
# 7) Visualization - Scatter + Regression Line
# ============================================
plt.figure(figsize=(8, 5))

# Scatter of actual data
plt.scatter(df["hours_studied"], df["exam_score"], label="Actual Data")

# Regression line using all X
y_line = model.predict(X)  # prediction for all hours_studied
plt.plot(df["hours_studied"], y_line, label="Regression Line")

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression: Hours Studied vs Exam Score")
plt.legend()
plt.grid(True)
plt.show()

# ============================================
# 8) Predict a New Value (Example)
# ============================================
new_hours = pd.DataFrame({"hours_studied": [5]})
predicted_score = model.predict(new_hours)[0]

print("\n===== Example Prediction =====")
print(f"Predicted exam score for 5 hours of study: {predicted_score:.2f}")

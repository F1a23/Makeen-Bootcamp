import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
data = {
    "Hours": [1,2,3,4,5,6,7,8,9,10],
    "Assignments": [1,2,3,3,4,5,6,6,7,8],
    "Score": [50,55,60,65,70,78,85,90,92,95]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Hours", "Assignments"]]
y = df["Score"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# ---- Plotting ----

# For plotting, vary Hours but fix Assignments at its mean value
hours_line = np.linspace(1, 10, 100)
assign_mean = df["Assignments"].mean()

X_line = np.column_stack([hours_line, np.full_like(hours_line, assign_mean)])

pred_line = model.predict(X_line)

# Create plot
plt.figure(figsize=(7,5))
plt.scatter(df["Hours"], df["Score"], label="Actual Data")
plt.plot(hours_line, pred_line, label="Best Fit Line", linewidth=2)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Multiple Linear Regression (Hours + Assignments)")
plt.legend()
plt.tight_layout()
plt.show()

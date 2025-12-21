import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# --------------------------------------------------
# 1. Collect Data
# --------------------------------------------------
df = pd.read_csv("data.csv")

print("Missing Values Check:")
print(df.isnull().sum())


# --------------------------------------------------
# 2. REPLACE Outliers in Target (price) using IQR (NOT REMOVE)
# --------------------------------------------------
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["price"] = np.where(
    df["price"] < lower_bound, lower_bound,
    np.where(df["price"] > upper_bound, upper_bound, df["price"])
)

print("\nOutliers replaced instead of removed.")


# --------------------------------------------------
#  FEATURE ENGINEERING
# --------------------------------------------------

df["house_age"] = 2025 - df["yr_built"]
df["is_renovated"] = df["yr_renovated"].apply(lambda x: 1 if x > 0 else 0)
df["total_sqft"] = df["sqft_living"] + df["sqft_above"] + df["sqft_basement"]
df["room_density"] = df["bedrooms"] / df["sqft_living"]

print("\nFeature Engineering applied.")


# --------------------------------------------------
# 4. Define Problem (Regression)
# --------------------------------------------------
X = df.drop("price", axis=1)
y = df["price"]


# --------------------------------------------------
# 5. Split Data into Train / Test
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# --------------------------------------------------
# 6. Identify Numerical and Categorical Features
# --------------------------------------------------
num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns


# --------------------------------------------------
# 7. Preprocessing Pipelines (Scaling + Encoding)
# --------------------------------------------------
num_pipeline = Pipeline([
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])


# ==================================================
# LINEAR REGRESSION MODEL ONLY
# ==================================================
lr_model = LinearRegression()

lr_pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", lr_model)
])

lr_pipeline.fit(X_train, y_train)


# --------------------------------------------------
# 8. Evaluate Model on Test Set
# --------------------------------------------------
lr_pred = lr_pipeline.predict(X_test)

lr_MSE = mean_squared_error(y_test, lr_pred)
lr_MAE = mean_absolute_error(y_test, lr_pred)
lr_RMSE = np.sqrt(lr_MSE)
lr_R2 = r2_score(y_test, lr_pred)

print("\n================ LINEAR REGRESSION RESULTS ================")
print("MSE:", lr_MSE)
print("MAE:", lr_MAE)
print("RMSE:", lr_RMSE)
print("R2 Score:", lr_R2)


# --------------------------------------------------
# 9. Inference: Predict House Price for One Sample
# --------------------------------------------------
sample = X.iloc[[0]]
prediction = lr_pipeline.predict(sample)

print("\nPredicted House Price:")
print(prediction[0])

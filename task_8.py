"""
What do you see here? What is happening here?
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

california_housing = fetch_california_housing()
X = california_housing.data
y = california_housing.target

df = pd.DataFrame(
    data=california_housing.data, columns=california_housing.feature_names
)
df["target"] = california_housing.target
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

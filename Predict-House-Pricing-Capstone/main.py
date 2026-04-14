import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('boston.csv')

print(data.shape)
print(data.head())
print(data.isna().sum())
print(data.duplicated().sum())

plt.figure(figsize=(10, 6), dpi=200)
sns.histplot(data['PRICE'], bins=50, kde=True, color='#2196f3')
plt.title('Distribution of House Prices in Boston')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
sns.histplot(data['RM'], bins=50, kde=True, color='#4caf50')
plt.title('Distribution of Rooms (RM)')
plt.show()

target = data['PRICE']
features = data.drop('PRICE', axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=10)

regr = LinearRegression()
regr.fit(X_train, y_train)

print("Training data r-squared:", regr.score(X_train, y_train))
print("Test data r-squared:", regr.score(X_test, y_test))
print("Intercept:", regr.intercept_)

coef_df = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
print(coef_df)

predicted_vals = regr.predict(X_train)
residuals = (y_train - predicted_vals)

plt.figure(figsize=(10, 6), dpi=200)
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title('Actual vs Predicted Prices (Training)')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.show()

plt.figure(figsize=(10, 6), dpi=200)
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values')
plt.xlabel('Predicted Prices')
plt.ylabel('Residuals')
plt.axhline(y=0, color='cyan', linestyle='--')
plt.show()

features_stats = features.mean().values.reshape(1, 13)
predicted_price = regr.predict(features_stats)[0]
print(f"Predicted price of an average Boston house: ${predicted_price * 1000:,.2f}")
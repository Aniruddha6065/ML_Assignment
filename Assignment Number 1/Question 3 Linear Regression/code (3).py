# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nGSOfHLg_sekWufV8n0fa-JZ6voB4CkA
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Load the dataset from a CSV file
data = pd.read_csv('salary_data.csv')
# Features and target variable
X = data[['Experience']] # Feature: Years of Experience
y = data['Salary'] # Target: Salary
# Create and train the model
model = LinearRegression()
model.fit(X, y)
# Take user input for prediction
user_experience = float(input("Enter years of experience: "))
# Predict salary for the user input
predicted_salary = model.predict([[user_experience]])[0]
print(f'Predicted Salary for {user_experience} years of experience: ${predicted_salary:.2f}')

# Calculate the Mean Squared Error (MSE)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
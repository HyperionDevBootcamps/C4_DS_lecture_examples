import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np

# Load data 
df = pd.read_csv('diabetes2.csv')

# Determine your independent and dependent variables
X = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
         'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].values
y = df['Outcome'].values # Diabetes outcome: 1 = yes, 0 = no

# Fitting the logistic regression model
clf = LogisticRegression().fit(X, y)

# Coefficients and intercept
print("Coefficients: ", clf.coef_)
print("Intercept: ", clf.intercept_)

# Make a prediction
y_pred = clf.predict([[0, 180, 70, 23, 94, 31, 0.351, 45]])
print("Outcome: ", y_pred)


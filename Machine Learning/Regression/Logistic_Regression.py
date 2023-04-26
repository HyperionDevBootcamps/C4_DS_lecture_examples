import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data 
df = pd.read_csv('diabetes2.csv')

# scatterplot to see patterns in our observations
sns.scatterplot(data=df, x='Glucose', y='Outcome')
plt.show()

# Determine your independent and dependent variables
X = df[['Glucose']].values
y = df['Outcome'].values # Diabetes outcome: 1 = yes, 0 = no

# Fitting the logistic regression model
clf = LogisticRegression().fit(X, y)

# Coefficients and intercept
print("Coefficients: ", clf.coef_)
print("Intercept: ", clf.intercept_)

# Make a prediction
y_pred1 = clf.predict([[120]])
print("Outcome for Glucose level of 120: ", y_pred1)

y_pred2 = clf.predict([[220]])
print("Outcome for Glucose level of 220: ", y_pred2)


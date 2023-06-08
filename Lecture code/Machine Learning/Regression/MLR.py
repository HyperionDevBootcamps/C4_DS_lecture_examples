import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('Advertising.csv')

# scatterplot to see patterns in our observations
sns.scatterplot(data=df, x='Radio', y='Sales')
plt.show()

# create three independent variables
X = df[['TV', 'Radio', 'Billboard']].values
# create dependent variable
y = df['Sales'].values

reg = LinearRegression()
model = reg.fit(X, y)

# regression cofficients and intercept
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)

print(reg.predict(np.array([[100,0,0]])))

# Fit the multiple linear regression model to make predictions
y_pred = reg.predict(X)

# Calculate R-squared
R_sq = r2_score(y, y_pred)

print("R-squared is ", R_sq)

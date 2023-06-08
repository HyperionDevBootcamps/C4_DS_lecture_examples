import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv('Advertising.csv')

# scatterplot to see patterns in our observations
sns.scatterplot(data=df, x='TV', y='Sales')
plt.show()


X = df[['TV']].values  
y = df['Sales'].values  
reg = LinearRegression()
reg.fit(X,y)

# fitting our regression model
y_pred = reg.predict(X)
plt.figure()
sns.scatterplot(data=df, x='TV', y='Sales')
plt.plot(X, y_pred)
plt.show()

# regression cofficient and intercept
print(reg.coef_)
print(reg.intercept_)

# predicted Sales value for a budget of $100000
print(reg.predict(np.array([[100]])))


# cross-validation to evaluate the model
scores = cross_val_score(reg, X.reshape(-1, 1), y, cv=5)
print("Cross-validation scores: {}".format(scores))

mean_score = np.mean(scores)  
std_score = np.std(scores)  

print("Mean cross-validation score: {:.2f}".format(mean_score))
print("Standard deviation of cross-validation scores: {:.2f}".format(std_score))
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.linear_model import LinearRegression

# dummy data
X, y = make_classification(n_samples=1000, n_features=10,
                           n_informative=5, n_redundant=0,
                           random_state=0, shuffle=False)

# splitting dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# models
linear = LinearRegression()
xgb_ = xgb.XGBRegressor()
forest = RandomForestClassifier()

# training models on training data
linear.fit(X_train, y_train)
xgb_.fit(X_train, y_train)
forest.fit(X_train, y_train)

# predictions for each model
pred_1 = linear.predict(X_test)
pred_2 = xgb_.predict(X_test)
pred_3 = forest.predict(X_test)

# see what we are working with
print("this is pred_1: ", pred_1)
print("this is the length of pred_1: ", len(pred_1))

# MSE for individual models
print("MSE pred_1:", mean_squared_error(y_test, pred_1))
print("MSE pred_2:", mean_squared_error(y_test, pred_2))
print("MSE pred_3:", mean_squared_error(y_test, pred_3))

# averaging model predicitions
final = (pred_1 + pred_2 + pred_3)/3

# MSE for ensemble model
print("Final MSE:", mean_squared_error(y_test, final))

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# read in your data
df = pd.read_excel("CreditRisk.xlsx")

# define your independent and dependent variables
X = df[['Volume', 'Value', 'Age']]
y = df['Status']

# encode your categorical variables
label = LabelEncoder()
X = X.apply(label.fit_transform)

# fit your tree model
tree = DecisionTreeClassifier()
tree = tree.fit(X, y)

# visualize the tree
plt.figure(figsize = (15,10))
plot_tree(tree, filled = True, feature_names = X.columns, class_names = ["Unpaid", "paid"])
plt.show()

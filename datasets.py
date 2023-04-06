# Demo code to show how to use pandas nad seaborn
import seaborn as sns

# loads test data
iris_df = sns.load_dataset("iris") # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# print(iris_df.columns)

# stores only the species
species = iris_df["species"]
# print(species)


# stores only the petal info
petal_info = iris_df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
# print(petal_info)


# stoes the petals smaller than 4.5
small_sepal_length = iris_df[iris_df["sepal_length"] < 4.5 ]
# print(small_sepal_length)


# stoes the mean for sepal width per species
mean_sepal_width = iris_df.groupby("species")["sepal_width"].mean()
# print(mean_sepal_width)


# import matplotlib to display charts
import matplotlib.pyplot as plt

# Shows the bar chart of sepal width average per species
plt.figure()
# passes data to display to the barplot method
# sns.barplot(x="sepal_width", y="species", data=iris_df)

sns.scatterplot(x="sepal_length", y="sepal_width", data=iris_df)

# displays chart 
plt.show()

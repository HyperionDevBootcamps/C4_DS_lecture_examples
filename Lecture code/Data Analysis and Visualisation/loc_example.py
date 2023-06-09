import seaborn as sns


# loads test data
iris_df = sns.load_dataset("iris") # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

print(iris_df) # Print out the dataframe



print(iris_df.loc[149]) # Returns row 149

## THE LOC ATTRIBUTE

print(iris_df.loc[0]) # Select the row at index 0 

# Slicing, up to 5
print(iris_df.loc[0:5])



# Specific columns
print(iris_df.loc[0, ["sepal_length","sepal_width"]])

print(iris_df.loc[:5 , :'petal_length']) # Select all the rows from 0 to 5. Columns  up to petal length

## THE ILOC ATTRIBUTE

#iloc select specific rows of the DataFrame based on their integer position

print(iris_df.iloc[:4]) # Up to the 4th integer  position

print(iris_df.iloc[:5, :2]) # Row up to 5, columns up to 2



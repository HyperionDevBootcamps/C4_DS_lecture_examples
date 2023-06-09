# Demo code for creating a class and then creating an object based on that class
"""
class Person:

    name = "Bob"
    age = 24


class Cat:
    # Class variable
    species = "Feline"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.paws = "Four paws"

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance method
    def speak(self, sound):
        return f"{self.name} meows: {sound}"

        # Instance method
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}, you are now {self.age} years old")


# Create an object of the Cat class
kitten = Cat("Felix", 2)
ginger_kitten = Cat("Ginger", 3)

# Access the object's attributes
print(kitten.name)
print(kitten.age)

# Call the object's methods
print(kitten.description()) 
print(kitten.speak("Meow Meow!"))
kitten.birthday()

print(kitten.age)
print(kitten.paws)

print(kitten.species)

kitten.species = "Test"

print(kitten.species)
print(ginger_kitten.species)

bob = Person()

print(bob.name)
"""

# additional resources on classes
# https://docs.python.org/3/tutorial/classes.html

# Demo on how to use a built in module
# Remember you don't need to run "pip install [module name]" for built in modules
"""
# imports the built in os module
# should usually be imported at the top of the file
import os

# Get the current directory path
current_root = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(current_root)

# Print the list of files
print(files)
"""

"""
# Demo on how to use a 3rd party module
# Remember to run "pip install pandas" in your terminal first

# imports the pandas module as pd so that pd can be called instead of pandas
# should usually be imported at the top of the file
import pandas as pd

# Read in the CSV file
df = pd.read_csv('data.csv')

# Print the first 5 rows of the data
print(df.head())

# Print the data types of each column
print(df.dtypes)

# Print some basic summary statistics of the data
print(df.describe())

"""
# Defining dictionaries

my_dict = {'key1': 'value1',
           'key2': 'value2',
           'key3': 'value3'}

value = my_dict['key1']
print("Contained in the first dictionary key we have:", value)

print("----------------------------------------------------------")

# Useful methods

keys = my_dict.keys()
values = my_dict.values()

# Adding and changing values to our dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict)
# call the variable with the new key we want and add the value
my_dict['key4'] = "value4"
print(my_dict)
# We can also do this with existing keys to change their value
my_dict['key2'] = [1,2,3,4,5]
print(my_dict)
my_dict['key2'][2] = "Three"
print(my_dict)

print("----------------------------------------------------------")

# Iterating through a dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for value in my_dict:
    print(my_dict[value])

print("----------------------------------------------------------")

# Example - we want to get the class average for a test

student = ["Angela", "Bruno", "Caleb", "Dan"]

# Define the q1 dictionary (marks out 0f 50)
q1 = {
    "Angela": 20,
    "Bruno": 16,
    "Caleb": 43,
    "Dan": 35
}

# Define the q2 dictionary (marks out of 50)
q2 = {
    "Angela": 30,
    "Bruno": 30,
    "Caleb": 48,
    "Dan": 38
}

# Calculate the total marks
total_marks = 0

for name in student:
    mark_value = q1[name] + q2[name]
    total_marks += mark_value

# Get the average

avg_mark = total_marks/4

# Print the result
print("Class average: ", avg_mark)

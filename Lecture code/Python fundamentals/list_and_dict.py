# Creates a list
# Lists are ordered by index and always start at index 0
"""
my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]
last_element = my_list[-1]
my_list[0] = 10
print(my_list)
"""


# Lists have the following methods that can be used with them
# NOTE to add a value to a list we must use append
"""
my_list = [3, 1, 4, 5, 2]
my_list.append(6)  # Add 6 to the end of the list
my_list.insert(0, 0)  # Insert 0 at the beginning of the list
my_list.remove(3)  # Remove the first occurrence of 3 from the list
popped_value = my_list.pop(0)  # Remove and return the last element of the list
my_list.sort()  # Sort the elements of the list in ascending order
my_list.reverse()  # Reverse the order of the elements in the list

print(my_list)
print(popped_value)

new_list = my_list.copy()
new_list.pop(0) 
print(new_list)
print(my_list)
"""

# Similar to Strings we can also use len on lists and itterate over them
"""
my_list = [1, 2, "Test", 4, 5]
print(len(my_list))

for item in my_list:
    print(item)
"""


# We can also use the "in" opperator to see if a value is in a list
"""
my_list = [1, 2, 3, 4, 5]
print("Test" in my_list)

if 6 in my_list:
    print("Value found in list")
"""


# Similar to strings we can also slice lists
# Slicing is done using the colon : operator. 
# For example, to get the first three elements of a list
"""
my_list = [1, 2, 3, 4, 5]
first_three = my_list[2:4]
print(first_three)
"""


# We can also Concatenate lists
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)
"""

# Lists can also store any mix of values, including other lists and dictionaries
"""
my_list = [1, "two", 3.14, False, ["This is list two", 2], {"test_dict": "Test Value"}]

print(my_list[5]["test_dict"])
"""

# Creates a basic Dictionary
# NOTE these function similar to a JSON
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value1 = my_dict['key1']
print(value1)
"""



# Similar to lists, Dictionaries have the following methods that can be used with them
# NOTE unlike list we don't need to use append to add a value
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dict_keys = my_dict.keys() # Return a list of all the keys in the dictionary.
dict_values = my_dict.values() # Return a list of all the values in the dictionary.

# Return the value associated with a key. If the key is not found, 
# return a default value (or None if no default value is provided).
get_value = my_dict.get('key4')
#dict_item = my_dict['key4'] 
#print(get_value)
#print(dict_item)

poped_value = my_dict.pop('key1') #Remove and return the value associated with a key.
print(poped_value)
print(my_dict)

del my_dict['key2']
print(my_dict)
"""


# To add a value to a dictionary, we simly need to do the following

"""
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
"""

# We can also loop over a dictionary
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for value in my_dict:
    print(my_dict[value])
"""

# We can also use the "in" opperator to see if a value is in a dictionary
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print('key5' in my_dict)
if 'key5' in my_dict:
    print('key1 exists in the dictionary')
"""

# We can also store any value in a dict or use any value as a ke
"""
my_dict = {1: 'The num', True: 'The bool', 3.14: 'The Float'}
#print(my_dict[True])
#print(my_dict)
my_dict[4] = "New Value"
#print(my_dict)
my_dict[4] = "New TEST Value"
#print(my_dict)

user = {"name": "Sanana", "password":"12345465"}

user_dict = {}
user_dict["id01"] = user

user = {"name": "Chris", "password":"password"}
user_dict["id02"] = user

#print(user_dict)

is_found = False
for user_id in user_dict:
    #print(user_dict[user_id])
    if user_dict[user_id]['name'] == "Jon":
        is_found = True

if is_found:
    print("Found User")
else:
    print("No user found")
"""

#new_dict = {"list1":[1,2,3,4,5], "list2":["a","b","c"]}
#new_dict.update({"list3":[1,2,3,4,5], "list4":["a","b","c"]})
#print(new_dict)
"""
new_list = [1,2,3,4,5]
new_string = ""
for i in new_list:
    new_string += str(i)

print(new_string)
"""

words = ["test", "new", "list", "of", "words"]
num = [1,2,3,4,5]
#sen = "*".join(words)
#print(sen)
new_dict = {}
for index, word in enumerate(words):
    new_dict[word] = num[index]

print(new_dict)
print(new_dict["new"])

help(print())
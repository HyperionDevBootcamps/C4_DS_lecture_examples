# This method returns the length of a string, 
# which is the number of characters in the string. 
# For example, the following code would print the length of the string "hello world":
"""
test = "hello  World"
print(len(test))
"""


# This method returns a new string with all the characters 
# in the original string converted to uppercase. 
# For example, the following code would print the string "HELLO WORLD
"""
test = "hello World"
print(test.upper())
"""

# This method returns a new string with all the characters 
# in the original string converted to lowercase. 
# For example, the following code would print the string "hello world"
"""
test = "HellO WorlD"
print(test.lower())

"""

# This method returns a new string with all occurrences 
# of a specified substring replaced with another substring. 
# For example, the following code would print the string "goodbye world":
"""
test = "hello World"
new_string = test.replace("o", "$", 1)
print(new_string)
"""

# This method removes any whitespace characters (such as spaces or newlines) 
# from the beginning and end of a string. 
# For example, the following code would print the string "hello world" 
# without any leading or trailing spaces
"""
test = "\thello\n world   "
new_string = test.strip()
print(test)
print(new_string.replace("\n", ""))
"""

# You can concatenate (i.e., join) two or more strings 
# using the "+" operator. 
# For example, the following code would print the string "hello world"
"""
test1 = "hello"
test2 = "world"
new_string = test1 + " " + "\n" + test2 * 3
pat = "#" * 50

print(new_string)
new_string = new_string.strip()
new_string = new_string.replace('\n', ' ')
print(pat)
print(new_string)
print(pat)
"""

# This method allows you to insert values into a string. 
# You can use curly braces {} as placeholders, which will be replaced 
# with the corresponding values passed to the method. 
# For example, the following code would print the string "My name is Alice and I am 25 years old"
"""
name = "Chris"
age = 25
test1 = "My name is {} and I am {} years old".format(name, age)
test2 = f"My name is {name} and I am {age} years old"
print(test1)
print(test2)
"""

# Include special characters (such as quotes or backslashes) in a string. 
# For example, the following code would print the string: She said, "Hello world"
"""
test = "She said, \"Hello world\""
print(test)
"""

# Use the "in" operator to check whether a substring is contained within a larger string. 
# For example, the following code would print "True"
"""
test = "hello world"
substring = "world"
print(substring in test)
"""

# NOTE: There are many options available for formatting strings in Python, 
# including specifying the width and precision of floating-point numbers, 
# adding leading zeros or spaces, and using different types of formatting syntax. 
# For example, the following code would print the string "The value of pi is approximately 3.14"
"""
pi = 3.141592653589793
test = "The value of pi is approximately {:.2f}".format(pi)
test = f"The value of pi is approximately {pi:.3f}"
print(test)
"""

# This method splits a string into a list of substrings 
# based on a specified separator. 
# For example, the following code would print a list containing the substrings "hello" and "world"
"""
test = "hello World"
substrings = test.split(" ")
print(substrings)
"""


# This method returns the index of the first occurrence 
# of a specified substring in a string. 
# For example, the following code would print the index 
# of the substring "world" in the string "hello world"
"""
test = "hello World"
index = test.index("o")
print(index)
"""

# You can extract a substring from a larger string using slicing. 
# Slicing involves specifying the start and end positions of the substring, 
# separated by a colon. 
# For example, the following code would print the substring "world" from the string "hello world"
"""
test = "hello World Test"
substring = test[6:-4]
print(substring)
"""

# Note that the colon can be used to specify both the start and end positions of the substring. 
# For example, the following code would print the substring "lo wo"
"""
test = "hello world"
substring = test[3:9]
print(substring)
"""


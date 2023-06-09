#  define a function using the "def" keyword, followed by the name of the function, 
# any parameters it takes (enclosed in parentheses), and a colon. 
# The body of the function should be indented. 
"""
def say_hello():
    print("Hello!")
# Once you've defined a function, you can call it by using its name followed by parentheses
#say_hello()

# You an also pass parameters to your function
# This function takes one parameter, "name", which is used to print a personalized greeting
def greet(number):
    print("Hello " + str(number) + "!" )

greet(1234)
"""

# Variables defined inside a function have limited scope, 
# meaning they can only be accessed within the function itself. 
# For example, consider the following code, when we try to print the value of "result" 
# outside the function, we get a NameError, since "result" only exists 
# within the function's scope.
"""
def double(x):
    result = x * 2
    print("Inside function: " + str(result))
    
x = 3
double(x)
print("Outside function: " + str(result))
"""

# Specify default values for function parameters
# These are used if the function is called without passing in a value for that parameter
# For example, the following code defines a function called "greet" 
# with a default value of "World" for the "name" paramete
"""
def greet(name="World"):
    print("Hello, " + name + "!")

greet()     # Output: "Hello, World!"
greet("Chris") # Output: "Hello, Bob!"
"""


# Functions can also return values, which can be used in other parts of your program. 
# To return a value from a function, use the "return" keyword 
# followed by the value to be returned. For example, 
# the following code defines a function called "double" that doubles its input and 
# returns the result
"""
def double(x=0, y=0, z=0):
    # exits the fuction and returns the result
    num = x * 2
    num2 = num + 4
    num3 = num2 + y
    num4 = num2 + z
    return num2, num3, num4

result1, result2, result3 = double(3, 1, 2)
print(result1)   
print(result2)  
print(result3)  
"""


# Sometimes you may want to define a function that can take a variable number of arguments. 
# To do this, use the "*" syntax to indicate a variable-length argument list. 
# For example, the following code defines a function called "sum" that can take 
# any number of arguments and returns their sum
"""
def add(*args):
    result = 0
    print(args)
    try:
        for arg in args:
            result += int(arg)
        return result
    except:
        print("Sorry wrong value")
        return 0

total1 = add("Bob")     
total2 = add("4", "5", "6", "7")   
print(total1)
print(total2)
"""

# Put it all together!
# Let's refactor code into functions

# EXAMPLE 1, refactor into a function that creates a dict that removes all occurances of an element
"""
my_list = ['a', 'b', 'c', 'a', 'd', 'a', 'e']

# Remove all occurrences of the element 'a'
# while 'a' in my_list:
#    my_list.remove('a')

def rem_list(at_list, item):

    while item in at_list:
        at_list.remove(item)
    return at_list

my_list = rem_list(my_list, "a")
print(my_list)
"""

# EXAMPLE 2, refactor into a function that creates a dict from two lists
"""
words = ["test", "new", "list", "of", "words"]
num = [1,2,3,4,5]
bool_list = [True, False, True, False, False]
# new_dict = {}
# for index, word in enumerate(words):
#    new_dict[word] = num[index]

def list_merge(keys_list, value_list):
    dict_to_return = {}
    for index, key in enumerate(keys_list):
        dict_to_return[key] = value_list[index]
    return dict_to_return

new_dict = list_merge(words, num)
print(new_dict)
new_dict2 = list_merge(num, bool_list)
print(new_dict2)
"""


# EXAMPLE 3, refactor into a function that creates a string from a list of numbers
"""
new_list = [1,2,3,4,5,7,8,9,10]
# new_string = ""
# for i in new_list:
#    new_string += str(i)

def num_list(number_list):
    new_string = ""
    for i in number_list:
        new_string += str(i)
    return new_string

returned_string = num_list(new_list)

print(returned_string)


var1, var2 = "1", "2"
list1, list2 = [], []
"""
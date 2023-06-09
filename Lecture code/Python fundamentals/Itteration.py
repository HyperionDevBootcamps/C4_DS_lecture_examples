
# Iteration using range()
# Saves current number of iteration as a variable called number
for value in range(10):
    # Displays current itteration
    print(value, end=" \" ")


# Iteration using a string
test = "This is a test"
# Saves current char of iteration as a variable called char
for value in test:
    # Displays current itteration
    print("$",value)


# Iterating with a while loop with numbers
num = 0
# Checks if number is less that 5 and continues to iterate while it's less than 5
while (num <= 5): # (num < 5) = True
    # Displays current value stored in num
    print(num, end = "")
    # Adds 1 to num to continue iteration
    # If not added this will result in an infinite loop
    num += 1


# Iterating with a while loop over a string
# resets num to 0 again
num = 0
some_string = "This String"
# Checks if number is less that the length of the string
while num < len(some_string):
    # Displays current char on the selected index
    print(some_string[num])
    # Adds 1 to num to continue iteration
    # If not added this will result in an infinite loop
    num += 1


is_looping = True

while is_looping:
    # Iteration using range() with an input
    user_select = input("Please enter the number of letters to display: ")
    test_string = "This is the string"
    try:
        user_select = int(user_select)
        if user_select > 0:
            # Saves current number of iteration as a variable called number
            for number in range(user_select):
            # Displays current itteration
                try:
                    print(f"Index {number} stores: {test_string[number]}")
                except:
                    print(f"Sorry {number} is out of range")
                    break
            break
        print("Sorry please enter a possitive number")
    except:
        print("Please enter a number using a numberical key")
        is_looping = False



# creates file to write to it
with open('test.txt', 'w') as file:
    file.write('1\n2\n')

total = 0

with open('test.txt', 'r') as file:
    lines = file.readlines()
    # itterates over line in lines variable to display content
    for line in lines:
        print(line.strip())
        total += int(line.strip())


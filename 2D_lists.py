# 2D List Example
# _____________
#      A   B   C 
#  1   1   2   3
#  2   4   5   6
#  3   7   8   9

# Converted to a 2D array

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Append new rows:
my_list.append([1, 2, 3])
# new list example:
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 2, 3]]
my_list.append([4, 5, 6])
# new list example:
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 2, 3], [4, 5, 6]]
my_list.append([7, 8, 9])
# new list example:
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# my_list = [
# [1, 2, 3], 
# [4, 5, 6], 
# [7, 8, 9], 
# [10, 11, 12], 
# [1, 2, 3], 
# [4, 5, 6], 
# [7, 8, 9]]

my_list.insert(4, [13, 14, 15])  # Insert 0 at the beginning of the list
# new list example:
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing and Changing Values
my_list[5][0] = 9
print(my_list)

# Display the list as 2D list
for row in my_list:
    for num in row:
        if num < 10:
            print(num, end=' ')
    print()
    
    





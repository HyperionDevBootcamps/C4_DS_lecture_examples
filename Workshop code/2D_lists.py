# What a 2D list looks like

'''
   A  B  C
1  0  1  2
2  3  4  5
3  6  7  8

'''
# Coverted into a 2D array

my_list = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Accessing values in a 2D lists

print("Second item in our first row: ", my_list[0][1]) # also the first item in second column

print("----------------------------------------------------------")

# Iterating through a 2D list

for row in my_list:
    print(row)
    for num in row:
        if num < 5:
            print(num, end = ' ')
    print()



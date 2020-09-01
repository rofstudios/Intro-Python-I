# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4) # similar to push in JS, adds it to the end of the list
print("1st ex ", x, " Appends 4 to the list")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x = x + y
print("2nd ex ", x, " Combines lists x & y")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8) # using remove function, pass value to remove
print("3rd ex ", x, " Removes value 8 of list")

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99) # First params takes position in list, second params takes new value to add
print("4th ex ", x, " Adding 99 to list on/after position 5")

# Print the length of list x
# YOUR CODE HERE
print(f"5th ex The length of list x is {len(x)}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print('6th ex ')
for i in x:
    print(i * 1000)
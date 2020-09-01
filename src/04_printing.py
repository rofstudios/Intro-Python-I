"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
print("%d, and %s" % (y, z))

# x is 10, y is 2.25, z is "I like turtles!"
print("x is %d, y is %.2f, z is %s" % (x, y, z))
# https://www.tutorialspoint.com/How-to-round-down-to-2-decimals-a-float-using-Python

# Use the 'format' string method to print the same thing
txt = "x is {x:d} y is {y:.2f} and z is {z:s}"
print("string format: " + txt.format(x = x, y = y, z = z))
txt2 = "using empty brackets: x is {} y is {} z is {}"
print(txt2.format(x, y, z))
# https://www.w3schools.com/python/ref_string_format.asp

# Finally, print the same thing using an f-string
print(f"using f string, x = {str(x)}, y is {str(round(y, 2))}, and z is {z}")
# https://www.knowledgehut.com/blog/programming/python-rounding-numbers
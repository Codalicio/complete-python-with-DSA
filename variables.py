# Variables are containers to store data.

'''
Variables in python are dynamically typed not statically typed,
as when defining a variable in python, we do not mention it's data type,
for example :
'''

x = 5
y = 4.6
z = "Raj"
a = True
b = [1, 2, "Amit"]
c = {1 : 'Amit', 'lastName' : 'Raj'}

print(a, b, c, x, y, z)

# Finding the type of the variables :
print(type(a), type(b), type(c), type(x), type(y), type(z))

# Finding the length of the variables :


name = "Amit Raj"
full_name = "Amit Raj"
age = 99

'''
In Python, everything is considered as an object.
As soon as we create a variable :
It gets stored in the memory with three attributes :
    1.). Type of the variable
    2.). Value of the variable
    3.). Reference count(number of variables with the same value)
'''
# id() :- built-in function to know the address of a variable :
print(id(name), id(full_name))
print(id(name) == id(full_name))

# In-built input() method :

userName = input("Enter your username : ")
print(userName)

# Data that we read from input() method will always be a 'string' by default :
age = input("Enter your age : ")
print(age, type(age))

# Output as a string :
# print() method can take multiple comma separated arguments :
print("Your username is", userName, "and your age is", age, ".")

# Using formatted string :
print(f"My username is {userName} and my age is {age}.")

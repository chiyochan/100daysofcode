# print statement
# In the print() function, you output multiple variables, separated by a comma
# You can also use the + operator to output multiple variables:

print("Hello World - trying out print statement")



# indentation minimum 1 space, common to have 4 spaces be consistent
if (5 > 2):
    print("5 > 2")

# Variables - variables are created when you assign a value to it
x = 5
print(x)

# Casting - If you want to specify the data type of a variable, this can be done with casting.
cx = str("Hello")
cy = int(4)
cz = float(5)
print(cx)


# You can get the data type of a variable with the type() function.
print(type(cz))

# String variables can be declared either by using single or double quotes
str1 = 'Single quote string'
str2 = 'Double quote string'
print(str1 , str2)


# Variable name
camelCase = 'camelCaseVarName'
PascalCase = 'PascalCaseVarName'
snake_case = 'snake_case_var_name'
print(camelCase + " " + PascalCase + " " + snake_case)


# Many values to many variables
vx, vy, vz = 'vx', 'vy', 'vz'
print(vx , ' ', vy, ' ', vz)


# Same value to multiple variables in one line
s1 = s2 = s3 = "same valueed variables"
print(s1, " ", s2, " ", s3)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
days = ["sun", "mon", "tue"]
ds, dm, dt = days
print(ds, " ", dm, " ", dt)

# Global variables - Variables that are created outside of a function (as in all of the examples above) are known as global variables.
glob_x = "global variable"

def func1():
  print(glob_x)

func1()

# Use the global keyword if you want to change a global variable inside a function.

def func2():
    global glob_x 
    glob_x = 'modified global variable'

func2()
print(glob_x)

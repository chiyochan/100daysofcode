# Check boolean condition
print ("Is 5 > 10: ", (5 > 10))

# Evaluate boolean value
print("Is 5 > 10: ", bool(5 > 10))

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
print("Boolean of Hello is : ", bool("Hello"))
print("Boolean of empty string is : ", bool(""))

# Any number is True, except 0.
print("Boolean of 0 is: ", bool(0))
print("Boolean of 3 is: ", bool(3))

# Any list, tuple, set, and dictionary are True, except empty ones.
print("Boolean of [1,2,3]", bool([1,2,3]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Functions can Return a Boolean
def returnTruePlease() :
    return True

print(returnTruePlease())



# Functions can Return a Boolean


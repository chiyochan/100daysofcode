# List comprehension: List comprehension offers a shorter syntax when you want to create 
# a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]
# The iterable can be any iterable object, like a list, tuple, set etc.
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
print("Sorting fruits ", sort(fruits))


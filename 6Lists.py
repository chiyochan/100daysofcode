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
fruits.sort()
print( "Sorting fruits ", fruits)

# Sort numerically
numLst = [500, 2, 75000, 500]
numLst.sort()
print("Sort numerically ascending ", numLst)

# Sort numerically descending
numLstDest = [345, 3000, 1, 2300]
numLstDest.sort(reverse = True)
print("Sort descending ", numLstDest)

# Custom sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Reverse  list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

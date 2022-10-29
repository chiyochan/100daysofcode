# A set is a collection which is unordered, unchangeable*, and unindexed. Duplicates Not Allowed.

set1 = {"blue", "cyan", "green", "indigo", "mauve"}
print("set1 ", set1)

# Access items
for s in set1:
    print(s)


# Check if indigo in set
print("Indigo in set? ", "indigo" in set1)

# To add one item to a set use the add() method.
set1.add("orange")
print("Added orange to set: ", set1)

# To add items from another set into the current set, use the update() method.
# The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).
set2 = {"yellow", "white", "violet"}
set1.update(set2)
print("Updated set: ",set1)

# To remove an item in a set, use the remove(), or the discard() method.
set1.remove("yellow")
print("After removing yellow: ", set1)
set1.discard("white")
print("After discarding white: ", set1)

# You can also use the pop() method to remove an item, but this method will remove the last item.
#  Remember that sets are unordered, so you will not know what item that gets removed.
set1.pop()
print("After popping an item ", set1)

# The clear() method empties the set:
set3 = {"a", "b", "c"}
print("set before clear() ", set3)
set3.clear()

print("set after clear() ", set3)

# The del keyword will delete the set completely:
set4 = {"d", "e", "f"}
print("set before del() ", set4)
del set4

# The union() method returns a new set with all items from both sets:
set5 = {1, 2, 3}
set6 = {4, 5, 6}
set5.union(set6)
print("Set5 union set6 ", set5)


# The update() method inserts the items in set2 into set1:
set7 = {7, 8, 9}
set8 = {10, 11, 12}
set7.update(set8)
print("Set7 union set8 ", set8)

# difference()	Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print("difference", z)


# difference_update()	Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print("difference update", x)

# intersection()	Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("intersection" ,z)


# isdisjoint()	Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print("Disjoint", z)

# issubset()	Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)

print("Is subset: ", z)

# issuperset()	Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)

print("Is superset: ", z)





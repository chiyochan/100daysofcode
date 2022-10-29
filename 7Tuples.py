# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

veggieTuple = ("avocado", "broccoli", "cauliflower", "eggplant")
print(veggieTuple)

# len() - number of items in tuple
print("Length ", len(veggieTuple))

# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
one_item_tuple = ("orange",)
print("one_item_tuple ", one_item_tuple)

# A tuple can contain different data types:
mixed_tuple = (1, True, "cherry")
print("mixed_tuple ", mixed_tuple)

# Access Tuple Items
print("Access element at 0 ", veggieTuple[0])
print("Access element at -1 ", veggieTuple[-1])

# Range of indexes
print("Range [1:3] ", veggieTuple[1:3])
print("Range [2:] ", veggieTuple[2:])
print("Range [:2] ", veggieTuple[:2])
print("Range [-2:-1] ", veggieTuple[-2:-1])

# To determine if a specified item is present in a tuple use the in keyword:
if "avocado" in veggieTuple:
    print("Yes, 'avocado' is in the veggie tuple")

# Change Tuple Values (although they are immutable)
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
veggieLst = list(veggieTuple)
veggieLst.append("tomato")
veggieTupleMod = tuple(veggieLst)
print("veggieTupleMod ", veggieTupleMod)

# Tuples are unchangeable, so you cannot remove items from it, but you can use the 
# same workaround as we used for changing and adding tuple items:
veggieLst.remove("eggplant")
veggieTupleRmv = tuple(veggieLst)
print("veggieTupleRmv ", veggieTupleRmv)

# The del keyword can delete the tuple completely:

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(veggie1, veggie2, veggie3, veggie4) = veggieTuple
print("veggie1 ", veggie1)
print("veggie2 ", veggie2)
print("veggie3 ", veggie3)
print("veggie4 ", veggie4)

# unpacking with *
(v1, v2, *v3) = veggieTuple
print("v1 ", v1)
print("v2 ", v2)
print("v2 ", v3)

# Loop Through a Tuple
for v in veggieTuple:
    print(v)

# To join two or more tuples you can use the + operator:
veggieTuple2 = ("potato", "zucchini")
veggieTuple3 = veggieTuple + veggieTuple2
print(veggieTuple3)

# Multiply tuple
multipliedTuple = veggieTuple * 2
print( multipliedTuple)

# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print("Number of times 5 occurs in the tuple ", x)

# Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print("First occurence of 8", x)









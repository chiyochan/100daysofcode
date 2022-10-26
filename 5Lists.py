# Create list
fruits = ["apples", "oranges", "bananas", "cherry", "kiwi", "melon", "mango"]
print("Created fruit list ", fruits)


# List Items: List items are ordered, changeable, and allow duplicate values.
# To determine how many items a list has, use the len() function:
print("Length of fruits list is: ", len(fruits))

# A list can contain different data types:
randomObjects = [True, 3j, "Goldilocks"]
print(type(randomObjects))

# use the list() constructor when creating a new list.
print("creating list with the list() constructor ", list([1, 2, 3]))

# Access list positive
print("Accessing list item with positive index", fruits[1])

# Access list negative
print("Accessing list item with positive index", fruits[-1])

# Return 3rd, 4th, and 5th item
print("Accessing sublist ", fruits[2:5])

# Get items from start to index
print("show first 3 items ", fruits[:2])

# Show last 3 items
print("Show last 3 items ",fruits[len(fruits)-3:])

# Change Item Value
fruits[0] = "Jackfruit"
print("Swapped apples with jackfruit ", fruits)

# Change a Range of Item Values
fruits[0:2] = ["TBD", "TBD", "TBD"]
print("Swapped a bunch with TBD ", fruits)

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
fruits.insert(0, "grapes")
print("Inserted grapes " , fruits)

# To add an item to the end of the list, use the append() method:
fruits.append("guava")
print("Appended guava ", fruits)

# To append elements from another list to the current list, use the extend() method.
exoticFruits = ["dragon fruit", "Durian"]
fruits.extend(exoticFruits)
print("Extended list ", fruits )

# The remove() method removes the specified item.
fruits.remove("TBD")
print("Removed one TBD ", fruits)

# The pop() method removes the specified index.
fruits.pop(1)
print("Removed TBD at index 1 ", fruits)

# The del keyword also removes the specified index:
del(fruits[1])
print("Removed TBD at index 1 ", fruits)

# The clear() method empties the list.
fruits.clear()
print("Cleared fruits", fruits)

fruits =['grapes', 'bananas', 'cherry', 'kiwi', 'melon', 'mango', 'guava', 'dragon fruit', 'Durian']
# You can loop through the list items by using a for loop:
for fruit in fruits:
    print(fruit)

# Use the range() and len() functions to create a suitable iterable.
for i in range(len(fruits)):
    print("using range: ", fruits[i])

# You can loop through the list items by using a while loop.
j = 0
while j < (len(fruits)-1):
    print("using while: ", fruits(j))
    j = j + 1










# List comprehension: List comprehension offers a shorter syntax when you want to create 
# a new list based on the values of an existing list.
# newlist = [expression for item in iterable if condition == True]
# The iterable can be any iterable object, like a list, tuple, set etc.
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list:

veggieList = ["broccoli", "carrot", "eggplant", "gourd", "jicama", "kale", "lemon", "mango"]
veggies_with_letter_g = [v for item in veggieList if 'g' in v]
print("veggies_with_letter_g ", veggies_with_letter_g)


# copy() - List copy
veggies = ["broccoli", "cauliflower", "eggplant", "ginger", "jicama", "kale"]
veggies_copied = veggies.copy()
print("veggies copied" ,veggies_copied)


# list() - copy with list
copied_again = list(veggies)
print("copied with list ", copied_again)

# + - join lists
fruits = ["apple", "banana", "canteloupe"]
produce = fruits + veggies
print("produce list ", produce)

# extend() add to existing list
groceries = ["detergent", "shrink wrap"]
groceries.extend(produce)
print("groceries ", groceries)
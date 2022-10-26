#T he format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.
# string.format(value1, value2...)

print("{city} is the best {place} in the world. ".format(city="NYC", place = "city"))
print("{0}, {1}, and {2} are very nutritious and affordable fruits ".format("Apples", "oranges", "bananas"))
print("{}, {}, and {} are cool months in the southwest ".format("November", "December", "January"))

# :<		Left aligns the result (within the available space)
print("Left align with 10 spaces {:<10} within the space".format("test"))

# :>		Right aligns the result (within the available space)
print("Right align {:>10} sample".format("test"))

# :^		Center aligns the result (within the available space)
print("Center align {:^15} sample  ".format("test"))

# :=		Places the sign to the left most position
print("The index changed up by {:=8} points".format(-10))

# :+		Use a plus sign to indicate if the result is positive or negative
print("Show me if {:+} is positive or negative ".format(10))

# :-		Use a minus sign for negative values only
print("Use :- to show if {} and {} are negative".format(-10, 10))

# :	Use a space to insert an extra space before positive numbers 
# (and a minus sign before negative numbers)
print("Use :  to add an extra space between the sign and numbers {: } and {: } are negative".format(-10, 10))


# :,		Use a comma as a thousand separator
print("Format :, {:,} thousand separator ".format(100000))

# :_		Use a underscore as a thousand separator
txt = "The watermelon is {:_} days old."
print(txt.format(1500000000))

# :b		Binary format
print("The binary version of 3 is {:b}".format(3))

# :d		Decimal format
txt = "We have {:d} books."
print(txt.format(0b101))

# :e		Scientific format, with a lower case e
print("There are {:e} planets".format(8))

# :E		Scientific format, with an upper case E
print("There are {:E} planets".format(8))

# :f		Fix point number format
print("There are {:f} continents".format(7))

# :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
print("There are {:F} continents".format(7))

# :g		General format
print("There are {:g} cakes".format(7.5))

# :G		General format (using a upper case E for scientific notations)
print("There are {:G} cakes".format(7.5))

# :o		Octal format
print("There are {:o} planets".format(8))

# :x		Hex format, lower case
print("There are {:x} planets".format(8))


# :X		Hex format, upper case
print("There are {:X} planets".format(8))

# :n		Number format
print("There are {:n} cakes".format(7.5))

# :%		Percentage format
print("There are {:%} women in the world".format(0.5))
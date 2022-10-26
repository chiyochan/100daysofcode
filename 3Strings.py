a = "Hello"
b = 'World'
print(a,b) 

# Multi-line strings
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)

# String as array
str1 = "Cool Kids"
print(str1[1])

# Looping through a string
for x in "banana":
    print(x)

# String length
print(len(str1))

# Check if string in text
if "ut" in c:
    print("ut found in c")

# Check if string not in text
if "banana" not in c:
    print("banana not found in c")

# Slicing the string
print('Slicing string', str1[0:5])

# Slice from start
print(str1[:5])

# Slice to end
print(str1[5:])

# Negative slice
print(str1[-5:-2])

# Upper case
print("this is a lower case sentance converted to upper".upper())

# Lower case
print("THIS IS AN UPPER CASE SENTANCE CONVERTED TO LOWER".lower())

# Remove whitespace
print(" Removing whitespace from this sentence ".strip())

# Replace string
print("bbbbbbbb replace with c".replace('b','c'))

# Split string
print("abababab".split('b'))

# Insert numbers in a string
ia = 5
ib = 10
print("Value of ia is {} and ib is {} ".format(ia,ib))

# Escape characters
print("I am trying to escape \" double quotes\" in my sentance")

# Converts the first character to upper case with capitalize()
print("i am going to capitalize this sentance".capitalize())

# Converts string into lower case with casefold
print("CONVERT TO LOWERCASE WITH CASEFOLD".casefold())

# Returns a centered string with center()
print("          ABC".center(0))

# Returns the number of times a specified value occurs in a string count
print("a a a a a".count('a'))

# Returns an encoded version of the string
print("Encode Ståle".encode())

# Returns true if the string ends with the specified value
print("I need to make some oats".endswith("oats"))

# Searches the string for a specified value and returns the position of where it was found - find()
print("My oats are not sweet even though I put maple syrup".find("sweet"))

# Searches the string for a specified value and returns the position of where it was found - index
print("My oats are not sweet even though I put maple syrup".index("sweet"))

# Returns True if all characters in the string are alphanumeric - isalNum()
print("Ab23ty_".isalnum())

# Returns True if all characters in the string are in the alphabet - isalpha
print("CoochieCoo".isalpha())

# UNCLEAR - returns True if all characters in the string are decimals - isdecimal
print("3.14".isdecimal())

# 	Returns True if all characters in the string are digits - isdigit
print("16734095".isdigit())

# isidentifier - A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
# A valid identifier cannot start with a number, or contain any spaces.
print("AUNER$%^_".isidentifier())

# 	isLower - Returns True if all characters in the string are lower case
print("asadsdads".islower())

# isnumeric - Returns True if all characters in the string are numeric
print("16734095".isnumeric())

# isspace() - Returns True if all characters in the string are whitespaces
print("Is space: " , "     ".isspace())

# istitle() method returns True if all words in a text start with a upper case letter, 
# AND the rest of the word are lower case letters, otherwise False.
print("istitle - ", "Keeper Of The Lost Cities".istitle())

# isupper()	Returns True if all characters in the string are upper case
print("isupper() - ", "I LOVE NY AND SF".isupper())

# join()	Joins the elements of an iterable to the end of the string
grains = ("rice", "wheat", "oats")
print(" ".join(grains))

# ljust()	Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# lower()	Converts a string into lower case
print("HARRY POTTER LOWER CASE".lower())

# lstrip()	Returns a left trim version of the string
print("lstrip", "     word".lstrip())

# maketrans()	Returns a translation table to be used in translations
str2 = "bl"
str3 = "fr"
trgt = "blog"
transtbl = trgt.maketrans(str2, str3)
print("Translated ", trgt.translate(transtbl))



# partition()	Returns a tuple where the string is parted into three parts
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
print("Apples bananas and oranges".partition("bananas"))



# replace()	Returns a string where a specified value is replaced with a specified value
print("replace: ", "The best city in the world is NY".replace("NY", "SF"))



# rfind()	Searches the string for a specified value and returns the last position of where it was found
# string.rfind(value, start, end)
print("rfind: ", "find the occurence of orange  orange".rfind("orange"))

# rindex()	Searches the string for a specified value and returns the last position of where it was found
print("rindex: ", "find the occurence of orange  orange".rindex("orange"))


# rjust()	Returns a right justified version of the string
# string.rjust(length, character)
print("orange".rjust(20, ","))

# rpartition()	Returns a tuple where the string is parted into three parts
# The rpartition() method searches for the last occurrence of a specified string, 
# and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
# The second element contains the specified string.
# The third element contains the part after the string.
print("Apples bananas and oranges".rpartition("bananas"))

# rsplit()	Splits the string at the specified separator, and returns a list
print("rsplit, apple, bananas, oranges".split(","))

# rstrip()	Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

# split()	Splits the string at the specified separator, and returns a list
print("split, apple, bananas, oranges".split(","))

# splitlines()	Splits the string at line breaks and returns a list
print("splitlines\nThis is a sample of splitLines.\nThere should be a newline here.")

# startswith()	Returns true if the string starts with the specified value
print("startsWith ", "This sentance startsWith This".startswith("This"))

# strip()	Returns a trimmed version of the string
print("    strip space sentance     ".strip())

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("Swapping Upper and lower Case".swapcase())

# title()	Converts the first character of each word to upper case
print("title -- harry potter and the half blooded prince".title())


# upper()	Converts a string into upper case
print("lower case converted to upper case".upper())

# zfill()	Fills the string with a specified number of 0 values at the beginning
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(25))
print(c.zfill(10))
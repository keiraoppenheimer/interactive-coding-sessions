print("Hello World") #In our python file (also called a Python script).
print("Hello friends") # Final way of running Python code: Run a script in full.

# What are the big variable types in Python?
this_string = "Quentin" # This is a string. 
# I assigned the value "Quentin" to the variable this_string
# This operation does not return anything.

this_float = 3.14 # This is a float
this_int = 12 # This is an integer
this_bool = False # Note the case-sensitive.

# What can you do with variables?
# Only after the line is executed do the variables exist in Python's memory. 
print(this_float) # Tab to autocomplete the current selection
print(this_string)

# What else can you print?
print(this_string) # You can print a variable
print("Hello") # You can print a 'literal'
print(12) # You are not storing it into a variable, you are directly printing an input.
print(12 + 5) # Printing an expression.
# SKILL: Being able to 'trace the code'. Meaning reconstruct the steps of a code. 
# Another example of an expression:
print(this_float + 5) # Here, we can again trace the steps.

# What is print()?
# print() is a function. A function is a way of doing something in Python.
# Functions are 'called' using ()
# Functions take a number of arguments (what goes inside the parenthesis)
# Some functions take zero, others take many.

# How many arguments does print() take?
# It can take one
print(this_float)
# ... but it can take more.
print(this_float, this_int, this_string)
# Print is printing all of its arguments on the same line.

# Let's do some calculations!
print(2 + 3) 
print(2 * 5)
print(2 + 3 * 5)
print( (2 + 3) * 5) # PEMDAS

print(0.1 + 0.2)

print ((0.1 + 0.2) == 0.3)
# Floating point error. Operations with decimal numbers are, by default, not mathematically 
# 'exact.'

# How can we avoid this?
# One way is to round: 
my_rounded_sum = round(0.1 + 0.2, 1)
print(my_rounded_sum)
print(my_rounded_sum == 0.3) # This is now true.

# More logical comparisons!
print(1 < 2)
print(1 > 2)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)

# You can also create more complex comparisons
print((1 < 2) and (3 > 2))
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) # Both true, so true
print(condition_1 and condition_3) # One False, so False
# AND requires ALL conditions to be True
# What about or?
print(condition_1 or condition_2)
print(condition_1 or condition_3) # True, why? 
# At least one of them is True.
# OR requires AT LEAST ONE condition to be True.
# Very important!

print(False + False) # ???
print(False + True)
print(True + True) # Now this is very weird
print(True == 1)
print(False == 0)

print(False * 5)
print(True * 3 + 1) # Simple stand-ins for 0 and 1

# Let's continue the weirdness.
greeting = "Hello " + "world!"
print(greeting) # The meaning of '+' changes when you apply it to 
# a string.
# +, when applied to strings, means 'concatenation': Bringing them
# into a single string.

laugh = "ha" * 3
print(laugh) # Here, * means 'repeat' when applied to a string.

weird_laugh = "ha" * 3.14 # Does not work!

my_age = 39
my_intro = "I'm Quentin and I'm " + my_age # Does not work.
# Returns a TypeError
# When you want types to work nicely with each other, you
# will need to convert them first.

# Let's see type conversions!
my_age_as_a_str = "39"
my_intro = "I'm Quentin and I'm " + my_age_as_a_str
print(my_intro)

# A better way to do that is to convert one type to the other
# using four nifty functions: str(), int(), float(), bool()

# How do we use them: 
print(str(42))
# Is this really a string?
type(str(42))
# Let's try others
str(3.14)
str(False)
str(0.1 + 0.2)
# We can convert pretty much anything to a string: int, bool, float

# Let's try float
float('Hello')
float('32')
float(False)
float(40)
float('fifteen')
# For float, it's sometimes going to work, sometimes not.

# Int?
int('Hello')
int(True)
int('32')
int(3.14) # Is it rounding or cutting off the decimal part?
int(3.9) # Option 2, not rounding!
round(3.9) # Gives us 4, not 3
# ANOTHER GREAT SKILL: Running experiments on your code.

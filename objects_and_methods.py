# Let's first recreate a variable or two.
my_integer = 10
my_str = "Hello world"
# I told you before that you can always see the tyep of a variable using type()
type(my_integer)
type(my_str)

# What is stored inside these objects?
my_str.upper # Upper is a METHOD that is attached to all the objects of class string.
# A method is like a function, so it needs to be CALLED. How do we call a function again?
# we put () after it.
my_str.upper() # Returning the upper, capitalized version of the string.
my_str.upper() # What does it mean "return a copy"?
# It means the original string is unchanged:
my_str
# Let's try another one:
my_str.lower() 
# What else is in there?
my_str.endswith('!') # Does not end with an exclamation mark
my_str.endswith('orld') # Returns true!
# Methods are a way of pairing functions to specific types of objects. 

# Some objects have other things than methods: Properties.
# Properties are information about the object that was created. 
my_integer.denominator # White wrenches are properties of the object
my_integer.numerator # Doe we put parenthesis? No.
# Properties are only meant to be read. They don't do anything. They just exist
# If something does not require any calculation to be given to you,
# and does not do anything, it is probably a property.
# But to be sure: look at the icon.
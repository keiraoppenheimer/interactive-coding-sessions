# Advanced topics in loops!

# Let's start with the concept of iterables.
# We have seen that we can loop over lists with for loops:

for i in [1, 2, 3, 4]:
    print(i)

# We can loop with for over ANYTHING that is iterable:
# Like a string!

for l in "Hello world":
    print(l) # We get the characters one at a time!

# In fact, you already knew that strings are iterable:
my_name = "Quentin"
my_name[0:4]

# What else can we iterate on
my_info = {"name": "Quentin", 
           "age": 39,
           "city": "Boulder"}

for k in my_info:
    print(k) # Going to get the keys!

# Iterating over a dict returns the keys.
# How can we get the value then?

for key in my_info:
    value = my_info[key]
    print(f"The current key is {key}, and its associated value is {value}") # How can we also get the value?

# It would be better if we could get both the key and the value 
# when iterating over a dictionary. Right?
# Turns out there is a way!

# ... But first a small detour:
my_fruits = ['banana', 'apple', 'mango']
first_fruit, second_fruit, third_fruit = ['banana', 'apple', 'mango']
name, age, city = "Quentin", 39, "Boulder"
# UNPACKING
print(first_fruit)

# Let's return to our dictionary
my_info.items()

for (key, value) in my_info.items():
    print(f"The key is {key}, and associated value {value}")

# Let's revisit the example of looping on my name:
my_name = "Quentin"
for letter in my_name:
    print(letter)

# I would like to know the index of each letter in my name.
# What is the position of each letter in my name?

# Whenever you face that, you have a great tool: enumerate()
# How does it work:
for (index, letter) in enumerate(my_name):
    print(f"The letter at position {index} is {letter}")

# The only thing that you need to do is:
# replace ITERABLE by enumerate(ITERABLE)
# replace step_variable by (index, step_variable)
# You can again use any variable name that you like,
# but the first one will receive the index, the second the element itself. 

a_list_of_food = ['pickle', 'pepper', 'peach']
a_list_of_tastes = ['sour', 'spicy', 'sweet']

# You can iterate over two lists (or multiple lists really) in parallel.
# All you have to do first is zip them.
for (food, taste) in zip(a_list_of_food, a_list_of_tastes):
    print(f"A {food} tastes {taste}")

# What if we also had the color of the foods?
a_list_of_colors = ['green', 'red', 'orange']

for (food, taste, color) in zip(a_list_of_food, a_list_of_tastes, a_list_of_colors):
    print(f"A {food} is {color} and tastes {taste}")

# The first thing that we're going to cover is a small utility to create lists 
# of numbers that we can loop on

# Let's say I wanted to print all the squares between 0 and 1,000:
# The way we did this so far, was something like this:
list_of_numbers = [0, 1, 2, 3, 4, 1000] # Not great
# It's called range()
# In its basic form, range works like this:
for i in range(1000): # It's the same thing as i in [0, 1, 2, 3, ..., 999]
    print(i ** 2)
# It takes one argument called stop: the value at which you will stop.
# You can also give two other arguments to range: start and step.
for i in range(3, 10, 2):
    print(i)
# The start, stop and step are things that we've seen for slicing
# They work in the same way for range, except that they create an iterable
# rather than slicing the values in an existing iterable. 
for i in range(5, 30, 5):
    print(i)

# Now for something slightly more complicated.
# Let's say we want to generate a list of all the squares of the numbers 1 through 9
# We'll do that using a for loop first. 
squares = []
for i in range(1,10):
    square = i ** 2 
    squares.append(square)
print(squares)
# We built a list one element at a time using a for loop.
# When you have to built a list (or any iterable) from another list (or another iterable)
# you will often encounter something called a LIST COMPREHENSION.
# It's simply a for loop, written in a more concise way, that builds a list.

squares = [i ** 2 for i in range(1, 10)]
# A list comprehension starts with square brackets: after all, we're building a list.
# Then an expression comes: here, it's (i ** 2).  It tells us how each element of the list
# is going to be constructed.
# Then, comes the loop, FOR STEP_VARIABLE IN ITERABLE. No colon, that's all.
print(squares)

# Let's try another example.
first_name = 'quentin'
whats_this = [x.upper() for x in first_name]

print(whats_this)

# You can add another "bell" to a list comprehension, an optional part of it:
# You can filter certain elements.

# We want to get the squares of all the numbers between 0 and 9, but ONLY
# if the square is less than 30.
small_squares = [i ** 2 for i in range(0, 10) if (i ** 2 < 30)]
# This is the exact same list comprehension as before EXCEPT
# We have an if statement. The if statement conditions whether an element
# will be added to the list or not. If, at a given iteration, the condition is false
# it is not added. If it is True, it is added.
print(small_squares)

# Let's say you have a folder full of mess. You're working with a disorganized
# colleague called Quentin.

folder_content = ["data.csv", "report.pdf", "summary.csv", "image.png", 
                  "notes.txt", "data2.csv", "archive.zip"]

# What I want: Filter out all the elements that are not .csv files.
# Reminder: You can check if a file name ends with .csv by using .endswith(".csv")
# It's a string method that returns True or False
# Try to write a list comprehension that will return a list with only the .csv files
list_of_csv_files = [i for i in folder_content if i.endswith("csv")]
print(list_of_csv_files)

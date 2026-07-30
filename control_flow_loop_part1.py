# If satements are about defining when (or whether) a block of code will run
# Loops are about defining how many times a block of code will run.
# It's about doing the same operations multiple times.
# We are going to learn about two types of loops today: 

# 1. While loops
# while keyword, followed by LOGICAL STATEMENT, followed by colon:

# In truth, you need a few other things:
# 1. Initialize th e parts of the logical statment.
count = 0 # The count exists, it has been defined
while count < 5:
    count = count + 1
    print(count)

# Inside, you have a code block again.
# 2. The second thing that a while loop needs is 
# that the content of the logical satement might change.
# Otherwise, it might loop forever. 

count = 0 # Initialized the condition
while count < 5:
    count = count + 1 # A variable that enters the condition is changing
    print(count)

# The skill: TRACING a loop.
# Understanding what is going to happen at each iteraction of the loop
# and how many times a loop is going to run.

# Iteration #, count
# First iteration, 1
# Second iteration, 2
# Third iteration, 3
# Fourth iteration, 4

# Second related skill:
# Predicting how many times a loop will run

# This isn't a particularly interesting while loop.
# More realistic examples

user_input = ""
while user_input == "":
    user_input = input("Please type something: ")
    print("The user typed: " + user_input)

# Another example: A to-do list
# Before we do that, I'm going to give a great trick.

age = 39
name = 'Quentin'
school = 'CU Boulder'
message = "My name is " + name + ", I am " + str(age) + " years old, and I teach at " + school
# How to combine variables with text, but its a bit of a PITA to write. 
# The gift of 'f-strings'
better_message = f"My name is {name}, I am {age} years old, and I teach at {school}"
print(better_message)

# Back to loops!
# A while loop with a to-do:
to_dos = ['walk the dog', 'mow the lawn', 'take out the trash', 'do the dishes']
while len(to_dos) != 0:
    item = to_dos.pop() # .pop() takes out the last element of the list, modifying it in place, and returns it. 
    print(f"I'm doing this: {item}. I still have these to do: {to_dos}")

# Let's try TRACING this loop:
# Iteration #, item, to_dos:
# First iteration, 'do the dishes', ['walk the dog', 'mow the lawn', 'take out the trash']
# Second iteration, 'take out the trash', ['walk the dog', 'mow the lawn']
# Third iteration, 'mow the lawn', ['walk the dog']
# Fourth iteration, 'walk the dog', []

# ANOTHER COMMON GOTCHA

# The second type of loop that exists in Python are FOR LOOPS.
list_of_numbers = [1, 2, 3, 4, 5]
for i in list_of_numbers:
    print(i)

# ANATOMY OF A FOR LOOP:
# It starts with for
# immediately after for is a variable name.
# It can be ANYTHING.
# Here it is i, but I could call it number, n, x, a... whatever
# This variable is called the STEP variable. It will take a different value at each 
# loop.
# Then the keyword in
# Then an ITERABLE: Any collection of items: Here, it is a list.

list_of_numbers = [1, 2, 3, 4, 5]
for i in list_of_numbers: 
    print(i)
# The for loops ITERATES over the elements of the ITERABLE
# storing each element into the STEP VARIABLE at each loop.

# Let's consider a slightly more complex for loop:
# We have a list of numbers, and we want to print their square:
list_of_numbers = [2, 3, 4, 5]
for number in list_of_numbers:
    square = number ** 2
    print(f"The square of {number} is {square}")

# Trace that loop before we run it:
# Iteration #, number, square
# First iteration, 2, 4
# Second iteration, 3, 9
# Third, 4, 16
# Fourth, 5, 25

# Let's ramp up the complexity a bit.
# We have printed all the squares of these numbers...
# but they haven't been stored anywhere
# It would be good to save them somewhere!

list_of_numbers = [2, 3, 4, 5]
list_of_squares = []
for number in list_of_numbers:
    square = number ** 2
    list_of_squares.append(square) # Appends the argument to the list, in place. IT does not return anything
    # Just edits the list
    print(f"The square of {number} is {square}, and our list of squares is now: {list_of_squares}")

print(list_of_squares)

# Iteration #, number, square, list_of_squares
# First iteration, 2, 4, [4]
# Second iteration, 3, 9, [4, 9]
# Third, 4, 16, [4, 9, 16]
# Fourth, 5, 25, [4, 9, 16, 25]

# Let's practice two others. 
# Let's write a for loop that can calculate the SUM of all numbers in a list. 
numbers_to_sum = [4, 8, 15, 16, 23, 42]
total = 0 
for number in numbers_to_sum:
    total = total + number
    print(f"The current number is {number}. The updated total is {total}")
print(total)
# How do we know if we have the right total?
print(total == sum(numbers_to_sum))

# Let's do the same thing for getting the MAXIMUM value in a list:
numbers = [-3, 5, 7, -12, 9, 31]

from math import inf
maximum = -inf

for x in numbers:
    if (x > maximum):
        maximum = x
    print(f"The current item is {x}. The new maximum value is {maximum}")
print(maximum == max(numbers))
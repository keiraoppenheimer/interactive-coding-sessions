# Talk about collections.
# Collections are different ways of storing things into a single variable.
# Up until now, when you were assigning content to a variable
# you were assigning a single thing:
a = "hello"
b = 3.14

# Now, we are going to learn (or-relearn) how to handle assigning multiple
# values to a single variable.

# We are going to cover two kinds of collections today. The first kind is LISTS:

my_empty_list = [] # Two squre brackets.
# This is a list:
type(my_empty_list)

# Lists are what are called ORDERED COLLECTIONS OF ITEMS.
# You can use it to store a sequence of other elements: 

my_favorite_numbers = [1, 2, 3, 4, 5] # You enter elements in a list by adding them
# between square brackets one at a time, separated by commas. 
# Lists can also contain strings!
my_favorite_colors = ['red', 'blue', 'green']
# Floats too!
my_favorite_floats = [3.14, 2.718, 1.618]
my_favorite_bools = [False, True, False] # Note that lists can contain
# repeated elements! They do not have to be unique.

# You can also put different things in a list:
my_mixed_list = [False, 3.14, 'Quentin', 1, True]

# You can even put lists inside a list!
my_list_of_lists = [[1,2], ["hello", 2], [False, 3.14]]

# You can really put anything you want inside a list.

# A list is, like most things in Python... an object!
# Meaning, lists are going to have... methods!

# Let's see what exists inside a list.
my_favorite_colors # Let's print it to remind ourselves what's in there.

# Let's check its methods:
my_favorite_colors.append # Append is a method for adding an element, or 
# several elements, to a list.
print(my_favorite_colors.append("purple"))
# When you run the append method on the list, it does not return anything.
# That's unlike what happens when you run a method on a string: It returns
# a transformation of the string:

my_name = 'quentin'
print(my_name.upper())

# So we ran a method on the list my_favorite_colors, and we did not get
# anything in return. What happened then?
print(my_favorite_colors) # That's strange!

print(my_name) # It is in lower case because when we run a method on a string,
# it returns a new string. It does not modify, or mutate, the orginal.

# With the list, we saw a mutation:
# After we ran the method append(), it changed the original content of the list
# it did not reurn anything, it changed the original list. 
# It mutated the original list.

# What would happen if we ran the method again?
my_favorite_colors.append('purple')
print(my_favorite_colors) # Every time you run append, it is adding additional 
# content to the original list. 

# Lists are MUTABLE, meaning their methods modify them directly. They DO NOT
# return a copy of the list. They change the content of the list.

# To know a list:
type(my_favorite_colors)
my_favorite_colors

# Let's learn another method on lists:
a = my_favorite_colors.pop() # Removes the last item of the list and returns it.
print(my_favorite_colors)
print(a)

# Now we've seen two methods: pop() (removes the last one and returns it)
# append() (adds something to the end of the list)
# One thing that we said was that lists are ordered.
# Because they are ordered, we can check what is located at a given position
# in the list. This is called INDEXING.

my_favorite_numbers = ['zero', 'one', 'two', 'three', 'four', 
                       'five', 'six', 'seven', 'eight', 'nine']
# To get the element located at a given INDEX in the list,
# we can use [i], where i is the INDEX of the element that we want to get. 

print(my_favorite_numbers[0])

# How would I get the 4th element of the list?
print(my_favorite_numbers[3])

# How would I get the 8th element?
print(my_favorite_numbers[7])

# What happens if I do this?
print(my_favorite_numbers[12]) # IndexError: Our list is shorter than that. 

# How would I grab the last element?
# Complicated way:
# How many elements are there in the list?
n_numbers = len(my_favorite_numbers) # len is a function that tells you
# how many things are inside a collection
my_favorite_numbers[n_numbers-1]
# Fortunately, there is a very nifty feature in python:
my_favorite_numbers[-1]
# What do you think this will print:
my_favorite_numbers[-2] # Second to last!

# That's called INDEXING: How we can grab a single element from a list.
# Now let's get more abitious: How do we grab MULTIPLE elements from a list?
# We can use something called SLICING:
# slicing works like this: my_list[start:stop:step]
# start tells you: where do we start in the list?
# stop tells you: where do we stop (index excluded)
# step tells you: how many items are we skipping?

# Let's do a few examples to understand how this works
my_favorite_numbers[0:5:1] # Grabs all the elements between index 0 and index 5
# (exclusive), don't skip any.
my_favorite_numbers[1:4:1] # Grab all the elements between 1 and 4 (exclusive), 
# don't skip any.
my_favorite_numbers[0:6:2] # All numbers between 0 and 6 (exclusive),
# skip every other number.

# You can omit some of these arguments when you slice:
my_favorite_numbers[0:5] # Here, which one did I omit? step!
# step, when omitted, defaults to 1. 
my_favorite_numbers[:6:1] # Which one did I omit? Start!
# start, when omitted, defaults to 0 
my_favorite_numbers[::1] # Which one(s) are omitted? Start and stop!
# stops defaults to the length of the list. 
my_favorite_numbers[::] # Which one(s) are omitted? All of them
# This gives you the full list.
# One note: A slice returns a COPY of the list. Meaning a NEW list. 

# Why the 'copy' matters
my_favorite_cities = ["Boulder", "Paris"]
lucas_favorite_cities = my_favorite_cities
print(my_favorite_cities) # Boulder and Paris
print(lucas_favorite_cities) # Boulder and Paris

# Now, I'm going to visit Barcelona. I loved it!
my_favorite_cities.append('Barcelona')
print(my_favorite_cities) 
# Lucas now visits Milan, and loves it!
lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities)

# In writing this: my_favorite_cities = lucas_favorite_cities
# I said: Lucas' favorite cities and mine are defined by the same list.
# Now let's redo the same exercise with a small change.

my_favorite_cities = ["Boulder", "Paris"]
lucas_favorite_cities = my_favorite_cities[::] # Creating a COPY of the list
# You can also do: my_favorite_cities.copy()
print(my_favorite_cities) # Boulder and Paris
print(lucas_favorite_cities) # Boulder and Paris

# Now, I'm going to visit Barcelona. I loved it!
my_favorite_cities.append('Barcelona')
print(my_favorite_cities) 
# Lucas now visits Milan, and loves it!
lucas_favorite_cities.append('Milan')
print(lucas_favorite_cities)

# Back to our main topic:
my_name = 'Quentin'
print(my_name[1:4]) # You can index and slice strings!
# Anything that is a collection and ordered, you can index.

# Since lists are mutables, you can do more than reading their content
# with indexing and slicing.
my_favorite_colors # ['red', 'blue', 'green', 'purple']
# Now, let's say something that my daughter says a lot: No,
# I don't like blue, I like PINK.
# First, where would we find 'blue' in the list?
# At the index one:
my_favorite_colors[1]
# So now how would you replace it?
my_favorite_colors[1] = "pink"
print(my_favorite_colors) # We just placed 'pink' at the position 1 of the list.
# and replaced whatever was there.

# If you want to add something in the middle of the list, you can use
# insert()
my_favorite_colors.insert(1, 'gold') # Is this going to print anything?
print(my_favorite_colors)

# Final thing: We can also swap multiple values at the same time:
my_favorite_colors[0:2] # We have a list with two elements
# If we want, we can substitute two other elements:
my_favorite_colors[0:2] = ['yellow', 'orange']
print(my_favorite_colors)
# What if the length sequence that you are trying to substitute does not match
# the length of the original
my_favorite_colors[0:2] = ['black']
my_favorite_colors # You can! You are replacing two values by one.

# There is just one final thing I want to show you:
my_name = "Quentin"
# We saw that, with a list, you can index and replace the value at that index
my_name[0] = "X" # STRINGS ARE IMMUTABLE
# You can only ever create a new one.
# You can read a string with indexinga and slicing, never ever write to it.

# Another type of collections called Dictionaries (or DICTS for short)
# A dictionary is a collection or key-value pairs. 
# There are key ('words') that have values ('definitions') much like a real
# word dictionary.

# Let me show you the syntax to create a dictionary"
my_friends_age = {"Nick": 40,
                  "Sam": 35,
                  "Juan": 37} # Curly brackets, and inside, you put key:value pairs,
# separated by commas. 
# Unlike lists, dictionaries are not ordered. They simply match values to keys

# The values in a dictionary can be of different kinds:
my_information = {
    "name": "Quentin", 
    "age" : 38, 
    "hobbies" : ["skiing", "birdwatching", "astrophotography"]
}
# For the keys, you have more restrictions:
# They are typically str, but sometimes int
# They must be unique
# They must be immutable objects. 

# How do we use a dictionary?
# Once you've created it, you can INDEX it with a key
# to know the value of that key:
my_friends_age['Nick']
my_information['hobbies'] # Keys are case-sensitive 
print('hobbies' == "Hobbies")
my_friends_age["Alice"] # KeyError: Alice is not a key that exists in that dict. 

# Dictionaries, much like lists, are MUTABLE
# Meaning we can reach into them and update a value associated with a key.
my_friends_age["Nick"] = 41 # We can reach into the dictionary with the key
# Nick, and replace the age with 41
my_friends_age # We have updated the value associated with the key Nick.
# How do we add a friend and their age?
my_friends_age["Alice:"] = 56 # Wei simply name the key and asssign it a value
my_friends_age

# Dictionaries are also OBJECTS. Meaning they have METHODS:
# Two useful methods. 
# Let's say we're not sure if a dictionary has a key 
# When we try to index with that key, we might get an error:
my_friends_age["Nico"] #KeyError!
# Errors aren't great because they stop your code.
# Instead, we can use a 'safe' method called 'get()'
my_friends_age.get("Nico") # If the key exists, it returns the value.
# if it doesn't, it returns None.

# If you want to delete a key from a dictionary
my_friends_age.pop("Sam") # Pop for a list takes a numerical index
# for a dict, it takes a key.
my_friends_age
# Three methods to see what is inside a dictionary:
my_friends_age.keys() # Prints all the keys that exist:
my_friends_age.values() # Prints all the values that exist:
my_friends_age.items() # Prints all the key-value pairs

# Final topic on dictionaries!
# Remember how I said values can be anything?
# Values can be dictionaries themselves!
# This is a very common data structure to represent users:

my_friends_info = {
    # Master dict: keys are going to be user names
    # and the values are going to be dictionaries containing
    # information about the users. 
    "Nick" : {
        "age" : 41,
        "hobbies" : ['basketball', 'cooking'],
        "city" : "Boulder"
    },
    "Sam" : {
        "age" : 35,
        "hobbies" : ['hiking', 'painting'],
        "city" : "Chicago"
    }
}

# How do we use a more complex data strucutre like this?
# How would you get  all of Nick's infos?
my_friends_info["Nick"] # What is the type of this objext that we just
# got? This is a dictionary!
# Let's double-check:
nicks_info = my_friends_info["Nick"]
print(type(nicks_info))
# So, if this is a dictionary... How can we get Nick's age directly from 
# my_friends)info?

(my_friends_info['Nick'])['age'] # You can always use parenthesis if that helps
# you make sense of the order in which the code is run.

# You know that you have a friend called Sam, but you're not sure
# if you have information about his hobbies
# Can you get his hobbies, and None if this info is not recorded?

my_friends_info["Sam"].get("hobbies")

# Nick recently picked up an exciting hobby: Sourdough baking!
# Can you add this hobby to Nick's list of hobbies?
# Hint: lists have the .append() method bound to them, that takes
# as argument the element that should be added to the list.

my_friends_info["Nick"]["hobbies"].append('sourdough baking')
my_friends_info

# Could I do that to add two hobbies in a row?
my_friends_info["Nick"]["hobbies"].append('sourdough baking').append("skydiving") #NoneType Error, append returns a none type
# because it just saves.
# Before we begin working on arrays, we are going to import a library
import numpy as np
import math 
# You reach into a library using dot notation:
print(math.pi)
print(math.sqrt(9))

# Let's create our first array together:

my_array = np.array([1, 2, 3, 4, 5]) # We are using the function 
# with a single argument: [1, 2, 3, 4, 5]
print(my_array)
# It looks a lot like a list.
# It contains elements, in order.
# We can index it:
print(my_array[0])
# We can slice it
print(my_array[0:3])
# So what's the difference really?

# Difference 1: Arrays can only contain elements of the same type. 
my_list = ['Quentin', False, 42]
print(type(my_list[0])) # str
print(type(my_list[1])) # bool
print(type(my_list[2])) # int

# Now let's try to create an array with the same content:
my_array = np.array(["Quentin", False, 42])
print(my_array)
print(type(my_array[1])) # str!

# All the elements were converted to strings.
# Why? Because arrays require all their elements to be of the same type. 
# When we create an array with multiple types, they all get converted (coerced)
# to a single compatible type. 
# Because arrays only contain a single type, they have what is called a DATA TYPE.
# dtype for short.
print(my_array.dtype) # Property called dtype.

int_array = np.array([1, 2, 3])
float_array = np.array([3.14, 2.76, 1.12])
bool_array = np.array([False, True, True])
print(int_array.dtype)
print(float_array.dtype)
print(bool_array.dtype)
# ARRAYS have a dtype, that conditions what lives inside of them.

# Second difference between lists and arrays:
# Arrays have a fixed size, something called a shape. 

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop(0)
print(my_list)
# The length of my list changed multiple times,
# It makes sense because lists have a lot of methods to add or remove elements:
# pop(), append(), insert()...

my_array = np.array([1, 2, 3, 4, 5])
my_array.append(6)
my_array.pop()
# You cannot change the length of an array. 
# You cannot add or remove elemnts from the array. 
# What you can do is create a new array with additional elements:
my_bigger_array = np.append(my_array, 6)
print(my_bigger_array) # I now have a bigger array...
print(my_array) # but the original array has not changed!

# Let's see what we can do with arrays that we could not do with lists:

# Suppose we sell five products. I'm going to write down their prices
# and quantitities sold:

prices = [9, 19, 4, 14, 24]
quantities = [120, 75, 300, 50, 40]
# P and Q for 5 different products

# Let's forget about arrays for a minute. Let's work with lists.
# I would like you to calculate, for each of the five items
# the total revenue: price * quantity.

revenues = []
for (p, q) in zip(prices, quantities):
    r = p * q 
    revenues.append(r)
print(revenues)
# This results in a list containing the revenues for the five items.

# This results into something like this:
arr_prices = np.array(prices)
arr_quantities = np.array(quantities)
# Now this is where the magic happens
arr_revenues = arr_prices * arr_quantities
print(arr_revenues)
# Python understands that you want the element-wise product of these two arrays.
# This operation is much simpler to write and is blaxing fast compared to a loop.
# This is because, under the hood, Python knows the type and shape of the arrays
# and does not have to do a lot of checks it would normally perform.

# Numpy implements "vectorized operations" that allow computers to work much faster.
# Let's see a few other examples showing how much nice it is to work with arrays:

# Sales for five products in two months:
sales_jan = np.array([120, 75, 300, 50, 40])
sales_feb = np.array([110, 60, 330, 80, 25])

# How much more did we sell in Jan compared to Feb?
diff = sales_feb - sales_jan
print(diff)

# By how much did the sales grow between January and February?
growth_rate = sales_feb/sales_jan
print(growth_rate)

whats_this = sales_feb == sales_jan 
print(whats_this)
whats_this_again = sales_feb >=  sales_jan
print(whats_this_again)

# What else? np contains a bunch of functions that can be applied to arrays:
np.sqrt(sales_jan) # Square root of all the jan sales
np.exp(sales_jan) # Exponential of all the jan sales

# Arrays have methods too!
sales_jan.mean() # Average sale volume across the five items.

# What can go wrong when working with arrays?
five_prices = np.array([1, 2, 3, 4, 5])
four_quantities = np.array([1, 2, 3, 4])
four_quantities * five_prices # To be added, multiplied, divided, compared, etc.
# arrays need to have compatible shapes:
print(four_quantities.shape)
print(five_prices.shape)
# Other common hiccup:
str_arr = np.array(["A", "B", "C", "D"])
str_arr + four_quantities # Working with incompatible dtypes. 

# Quick refresher on indexing:
# We can use indexing to access a value:
arr_prices = np.array([5, 10, 15, 20, 25])
print(arr_prices[0])
# We can also use indexing to replace a value "in place":
arr_prices[0] = 20
print(arr_prices)

# We can also use slicing to access values:
print(arr_prices[0:3])
# ... and to replace values:
arr_prices[0:3] = [7, 14, 21]
print(arr_prices)

# These two behaviors are common to lists and arrays.
# With arrays, you can do two more things:

# 1. Boolean Indexing, or Masking.
arr_prices = np.array([7, 14, 21, 20, 25])
mask = [False, False, True, True, False]
arr_prices[mask] # I am using square brackets, and using the mask as an index.
# All the elements that had a False in front of them were omitted, and only the
# elements that had a True in front of them were returned by indexing.

# I'm going to show you useful examples of how these masks and Boolean indexing is used.

# Example 1:
arr_q = np.array([10, 20, -5, -2, 4, 10]) # It is obvious that this array contains errors.
# You cannot sell negative items. 
# Now imagine we have 1000 quantities like this. We cannot inspect, by hand,
# which ones are negative.  How could we use a mask to flag all of the negative values?

# (i) Create a mask that identifies the negative values.
# (ii) Use the mask to index all the negative values in the array.

# Correct by inefficient!
mask = []
for q in arr_q:
    if q >= 0:
        mask.append(False)
    else:
        mask.append(True)

mask = arr_q < 0 # This is going to check how each of the array elements compare to 0
# True if smaller, False otherwise.
print(mask) # First step: Done! We have the mask.

# How can we use the mask now, to get the negative values from the array?
arr_q[mask] # Why does it work again?
# Our mask is F, F, T, T, F, F
# When we put it in front of [10, 20, -5, -2, 4, 10], we get [-5, -2]

# We used the mask to see exactly which quantities were less than zero.

# (iii) Can we fix these errors? Can we use the mask to replace all the negative
# quantities with zero instead?

arr_q[mask] = 0 # Remember that you can use indexing to read, but also replace, values.
print(arr_q) 

# Bonus one-liner:
arr_q[arr_q < 0] = 0 # Indexing arr_q using the mask (arr_q < 0), then assign the value
# 0 to all these indices.

bakery_visits = np.array([0, 15, 12, 8, 9, 0, 5])
# These are the visits to a bakery, Mon-Sun

# (i) How many visits did the bakery get per day on average (hint: use the .mean() method)
# (ii) Are there any days where the bakery did not get any visits? Show them using an index.
# (iii) Excluding the days where the bakery did not get any visits,
# how many visitors did it get? (hint use the .mean() method again).

bakery_visits.mean() # On average, our little bakery is getting 7/day

mask_zero_visitors = (bakery_visits == 0)
print(mask_zero_visitors)
bakery_visits[mask_zero_visitors]

bakery_visits[bakery_visits < 1]

bakery_visits[bakery_visits > 0].mean() # This is correct, we can decompose it:
mask_some_visitors = (bakery_visits > 0)
bakery_visits[mask_some_visitors].mean()


# The second thing you can do with arrays, and not lists, is much simpler
# also has a cool name: "Fancy" indexing.

arr_words = np.array(["The", "Quick", "Brown", "Fox"])
# Fancy indexing simply means giving a list of indices that you want the values of:

desired_indices = [0, 1, 3]
arr_words[desired_indices] # I index using the list of indices I want.

# You can also repeat positions:
desired_indices = [0, 1, 3, 0, 1, 2]
arr_words[desired_indices]

# What's the use of fancy indexing?
# Most common use is randomly selecting rows in a dataset.

# Exactly like indexing, but you can use a list of numbers rather than just one.
# You can also skip the variable definition:
arr_words[[0, 1, 0, 1, 3]] # Note the double bracket: First one to say "I'm indexing", 
# second one to say "this is a list of indices"
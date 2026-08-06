import numpy as np

# Reminder: This is an array
one_d = np.array([1, 2, 3, 4, 5,])

# You  might remember that arrays have a shape:
one_d.shape

# We are going to create our first 2-D array

two_d = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
print(two_d)
# I see two lines, corresponding to the number of sublists
# and three columns, corresponding to the number of elements in each sublist.
# If the sublists do not have the same number of elements, 
# you are going to get an error. 

# Now we have a 2-D array, let's look at its shape:
print(two_d.shape)
# With a matrix, the first element of the shape is always the number of ROWS
# the second is always the number of COLUMNS. 

# A 2D array is... an array!
print(type(two_d))
print(type(one_d))
# They are going tow ork in extremely similar ways to one-dimensional arrays.
# One term that you might see so I'm giving it to you:
# 1D array is a vecotr
# 2D array is a matrix
# a single element is a scalar

# Ok, so if 2D arrays are array, we can probably index them.
# Let's see how that works:
print(two_d)
print(two_d[0]) # If you give a single index to a matrix, you get the row
# corresponding to that number
print(two_d[-1]) # Final row of the matrix.

# We can also do slices on 2D arrays:
print(two_d[0:2]) # The first two rows of my matrix.
print(two_d[0:1])

print(one_d) # A small but important aside:
print(one_d[0]) # Only one element, a scaler
print(one_d[0:1])

# Now back to 2D arrays:
print(two_d[0]) # A 1D array.
print(two_d[0:1]) # A 2D array, with just one row.

# So what about columns now?
# When we index a 2D array with a single number, 
# we are getting a single row. 
# When we index a 2D array with a single slice,
# we are getting a subset of the rows. 

# How do we slice and index on columns?

print(two_d[0,0]) # This means: "Row 0, Column 0"
print(two_d[0, 2]) # First row, third column.
print(two_d[-1, -1]) # Last row, last column

# What if you want ALL the rows?
print(two_d[:,1]) # ':' means "ALL OF THEM"
print(two_d[:, 0:2]) 

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Exercise 1: Using indexing, replace the element 5 by 999
two_d[1,1] = 999
print(two_d)

# Exercise 2: Replace the final column by [7, 14, 21]
two_d[:, 2] = 7, 14, 21
print(two_d)

# Exercise 3: Double the values in the first row.
two_d[0, :] = two_d[0, :] * 2
print(two_d)

two_d = np.array([
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
])

# Exercise 4: Replace all the negative values in the matrix by 0s. 
# a) Write a mask matrix that contains True where all the negative values are in two_d
# b) Use the mask to print all these negative values 
# c) Use the mask to replace the negative values by 0s

mask = two_d < 0
print(mask) # Step (a) is done.

# Step b
print(two_d[mask])

# Step c. 
two_d[mask] = 0 
print(two_d) # We are replacing the negative numbers by zeros in the original matrix.

# We already saw on Tuesday that the main benefit of arrays is that you can
# add, multiply, divide, or subtract them, as long as they have compatible shapes.

# The same is true of matrices, because they are arrays:

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [1,1],
    [2, 4]
])
print(a+b)
print(a-b)
print(a/b)
print(a*b)

# Same as Tuesday. 

# 2D arrays have the same methods as 1D arrays, with a very small twist.

units_sold = np.array([
    # How many items of products A, B, and C were
    # sold in months Jan-Apr
    [120, 150, 130, 170],
    [75, 60, 90, 80],
    [300, 330, 310, 350]
])

print(units_sold)
# You probably remember that arrays have methods like sum(), mean(), min(), max():
# What happens if we do :
print(units_sold.mean()) # This is what we sometimes call the GRAND mean:
# The mean of all the products sales across all months and all products.

# When you have matrix data, it can be nice to get the means by rows
# and by columns instead. Means by rows would mean: "Average sales of each product
# across the 4 months", means by columns would mean: "Average sales for each month
# across the three products". 

# How can you do that?
# The methods have a magic keyword called axis.
# Axis tells you on which axis you are summarizing. 
print(units_sold.mean(axis=0)) # It means: We average across the axis 0, which are the rows.
# The rows are going to disappear, and we will have mean per column
# If instead, we do:
print(units_sold.mean(axis=1))
# The axis specifies the axis that will disappear. On which the method will be applied. 

# Exercise 1: The method min() gives you the minimum of an array.
# Use this method to find the smallest amount sold across the four months
# for each of the 3 products.

print(units_sold.min(axis=1))

# Find the largest sale generated for any product across the four months
print(units_sold.max())

# Final one:
# Find the largest sale for product A.
print(units_sold[0, :].max())
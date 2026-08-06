import pandas as pd

# Let's write a dictionary.
data = {
    "Month": ["January", "February", "March", "April"],
    "Marketing_Spend": [5000, 7000, 6000, 8000],
    "Sales_Spend" : [2000, 3000, 2500, 4000],
    "Leads_Generated" : [150, 200, 180, 250]
}

# This dictionary is not a dataframe, but it's a very good mental model
# for thinking about dataframes:
# The columns are like keys in a dictionary.
# And the values are arrays/lists that all have the same number of elements.
# They correspond to the rows. 

# In fact, a very common way of creating a dataframe by hand
# is to create it from a dictionary:
df = pd.DataFrame(data)
print(df)

# As you might guess, it is pretty uncommon to type the values one by one 
# into Python... what is much more common is to read the content of a file
# into a dataframe:
df = pd.read_csv("sales_data.csv") # Relative path! 

# The first thing that you should do after loading data
# is inspect your data:
print(df)
# If you print a very big dataframe, your terminal will crash
# A better way is to just print the first and last few rows
print(df.head()) # First five rows:
print(df.tail()) # Last five rows:

# Second inspection: 
print(df.info())

# If you need to access each of these info individually, you can:

print(df.columns)
print(df.index)
print(df.shape)
print(df.dtypes)

# Actually working with dataframes.
# You can read the content of columns in your data by indexing: 
print(df["Month"]) # Individual columns in dataframes are called Series
print(type(df["Month"])) # Series are like arrays with an index in front.

# You can also ask for multiple columns:

print(df[["Month", "Sales_Spend"]]) # We index with a list of column names
# You get a dataframe.

# Again, repeating some content
# You can read with indexing...
# and you can assign values with indexing!

# Exercise 1: Increase the sales_spend by 100 (+100) and save it into the data frame
df["Sales_Spend"] = df["Sales_Spend"] + 100 # We are getting the content of the column
# modifying it, and putting it back into the dataframe.
print(df[["Sales_Spend"]])

# What is new is that we can also use indexing to create new columns:
# Let's say we want to calculate the cost per lead:
print(df["Marketing_Spend"] / df["Leads_Generated"])
# How do we add these values to a column in the dataframe
df["Cost_Per_Lead"] = df["Marketing_Spend"] / df["Leads_Generated"]
print(df.head())

# Another common operation is to filter the dataframe.
# Let's say we want to see which months were particularly effective
# in acquiring leads. We want to see on which months the costs of 
# acquiring leads was less than 15. 

# Let's create a mask: Something that, for each row, 
# contains True or False, depending on whether Cost_Per_Lead was < 15.

mask = df["Cost_Per_Lead"] < 15
print(mask)
# The next step is to apply the mask:
df[mask]

# Wait what?
# We've used df[index] BOTH to index columns (using a column name or list of names)
# but ALSO df[mask] to index rows (using a mask)

# Fortunately, they later introduced a more correct and more intuitive way
# of indexing dataframes:

# The syntax is df.loc[row_index, col_index]

# Let's say I want to see all the rows, and just the columns Marketing_Spend and 
# Sales_Spend:
df.loc[:, ["Marketing_Spend", "Sales_Spend"]]

df.loc[[0, 2, 4], ["Marketing_Spend", "Sales_Spend"]] # Just line 0, line 2, line 3
# with the same columns.

# It's like indexing a matrix, except we are using the name of the rows
# and the name of the columns. 

df.loc[:, "Sales_Spend"]

# 1. ALWAYS USE .LOC to index a dataframe
# 2. Remember that the first indexer is ROWS, the second is COLUMN.
# 3. Remember that we are using the NAMES of the rows and columns, not their position
# to index them (or a mask). 

shorter_df = df.loc[[5, 6, 7], ["Marketing_Spend", "Sales_Spend"]]
shorter_df.loc[0, :]

# Skill 2: Summarizing data.

# Both dataframes and series have methods. You can use them to get the mean(), 
# the min(), the max()...

df.loc[:, "Cost_Per_Lead"] # Here I get a series.
df.loc[:, "Cost_Per_Lead"].mean() # I get the mean of that column across all the rows.

# What about calling methods on a dataframe?

df.loc[:, ["Sales_Spend", "Marketing_Spend"]] # This gives me a dataframe with two columns.
df.loc[:, ["Sales_Spend", "Marketing_Spend"]].mean()
# When you call a method to summarize a dataframe with numeric columns,
# you are getting one value per column. Here, we get the average marketing spend
# and the average sales spend, taken across all the rows.

# Now consider this second example:
df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum() # This time, I want to get the sum
# of the Sales_Spend and the Marketing_Spend, but not at the column level, I want them
# at the row level: I want to know, for each month, how much we spend in sum
# on Marketing and Sales combined.
# But that's not what I'm getting here.

df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum(axis=1)
# To sum across the columns, we need to set axis = 1
# Much like on matrices.
df["Total_Spend"] = df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum(axis=1)
df.loc[:, "Total_Spend"] = df.loc[:, ["Sales_Spend", "Marketing_Spend"]].sum(axis=1)
# Two ways of doing it

print(df.head())

# Great job! We've done some basic data cleaning and manipulation with pandas.
# Last step is to save our dataframe back into a file: 
df.to_csv("sales_data_cleaned.csv", index = False) # Thanks, but no thanks, no index.
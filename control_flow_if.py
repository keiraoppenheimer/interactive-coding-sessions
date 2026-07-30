# We are going to talk about control flow. 
# Control flow is instructions that determine when, whether, and how often
# a section of the code is going to run.

my_name = "Quentin"
my_gender = "Don't know"

if my_gender == 'Male':
    print("Hello Mr. " + my_name)
elif my_gender == 'Female':
    print('Hello Ms. ' + my_name)
elif my_gender == 'Non-Binary':
    print("Hello " + my_name)
else:
    print("Hello " + my_name + ", how should I adress you?")

# ANATOMY OF AN IF STATEMENT
# An if statement begins wtih a keyword if: 
# After the if statement, we have: a logical statement, or logical test,
# or logical expression is any expression that is going to evaluate to True or False
# after that, a colon: 
# On the next line follows and INDENTED CODE BLOCK:
# The indented code block is what the machine will run IF the logical statement 
# evaluates to True. Otherwise it will NOT run.

# After this code block, you can have between zero and many ELIF statments. 
# Strucutre: elif LOGICAL_STATMENT: 
# each followed by their own code block 
# When will these code blocks run?
# 1. When the logical statement is True AND
# 2. None of the PREVIOUS ones were True. 
# Conditional logic blocks run sequentially, one statement at a time.
# And they stop at the first True statement that they encounter.
# The FINAL statement can be (but does not have to be) an ELSE statement:
# else: # Note that there is no condition. 
# When is the else block going to run?
# ONLY when ALL the statements have evaluated to False. 

# VERY COMMON GOTCHA WITH CONDITIONAL STATEMENTS:

def status_checker(age):
    if age >= 13:
        print("You are a teenager")
    elif age >= 18:
        print("You are an adult")
    elif age >= 4:
        print("You are a kid")
    else:
        print("You are a baby")

status_checker(1)
status_checker(5)
status_checker(17)
status_checker(39)

def correct_status_checker(age):
    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    elif age >= 4:
        print("You are a kid")
    else:
        print("You are a baby")

# ALWAYS CHECK THE MOST RESTRICTIVE CONDITION FIRST:

def can_legally_drink(country, age):
    if (country == 'USA'):
        if (age >= 21):
            return True
        else:
            return False
    elif (country == 'Canada'):
        if (age >= 19):
            return True
        else:
            return False
    elif (country == 'Germany'):
        if (age >= 16):
            return True
        else:
            return False
    else:
        return "Don't know"

# Trick 1: You can write a simple if statement in one line.
# That's allowed, it's called the "TERNARY OPERATOR": 
age = 20

status = "Adult" if age >= 18 else "Minor"

# VALUE_IF_TRUE if LOGICAL STATEMENT else VALUE_IF_FALSE
if age >= 18:
    status = 'Adult'
else:
    status = 'Minor'

# Trick # 2
# You can sometimes save yourself a lot of effor by using a dictionary
# rather than an if statement.

# Let's say you want to map countries to their currency:

def get_country_currency(country):
    if country == "USA":
        return "US Dollars"
    elif country == "Canada":
        return "Canadian Dollars"
    elif country == "France":
        return "euros"
    elif country == "Japan":
        return "Yen"
    else: 
        return "Country not found"
# Good, but not great.
# Let's take a step back. What are we doing here?
# We are always checking the value of one variable
# (country) and depending on the value, returning another value.

# It works a lot like a dictionary!
country_currency = {
    "USA": "US Dollars", 
    "Canada": "Canadian Dollars",
    "France": "Euros",
    "Japan" : "Yen"
}
# How do we get the currency?
country_currency["France"]

# Wait a minute... This is NOT the same thing?
get_country_currency("Iran") # Country not found!
country_currency["Iran"] #KeyError

# However...
country_currency.get('Iran', "Country not found")
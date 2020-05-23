# function with optional arggument

def hello(yes, no, maybe=''):
    return print(yes,no,maybe)

hello('yes','yes')
hello('yes','yes','yes')

# Funtion that pass arbitrary number of arguments

def hello(*yo):
    print(yo)

hello({'ahmed':'yes'},{'ahmed':'yes'},{'ahmed':'yes'})

# Somtimes we know two or three things about the user but he might enter more information
# so we want to pass as many information that the user enter to our database
#So here we can build a dictionary that accept new informations from the user.

def build_prilfe(first, last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user = build_prilfe('albert','einstein', location='pricenton', field='physics')
print(user)


"""
We can call a function from a module easily using this:

module_name.function_name()

Standard way to import a function :

from module_name import function_name

we can give it a new name as the following:
from module_name import function_name as fn

importing all functions in a module
from module_name import *



"""

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


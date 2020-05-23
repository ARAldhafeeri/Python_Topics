# Using json.dump() and json.load()
import json

numbers = [2,3,4,5,7,11,13]
# dumping files into a json
filename= 'numbers.json'
with open(filename, 'w') as f:
        json.dump(numbers, f)

# loading files from a json.
filename= 'numbers.json'
with open(filename, 'w') as f:
        json.load(f)

file= 'users.json'
with open(file, 'w') as f:
        name =input("enter your name")
        last = input("enter your lastname")
        email = input("enter your email")
        json.dump("[[{}],[{}],[{}]]".format(name,last,email))

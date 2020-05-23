my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

"""
THis won't work:
friend_foods = my_foods

because python will make both variables point to the same newlist
if that what we want then it is correct
The resson is python will only associate the variable friend_foods with my_food
Put using the method above is the correct way of copying the elements of a list into another one

"""
print(friend_foods)

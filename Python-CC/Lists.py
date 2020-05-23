bicycles = ['terk','cannodale','redline','specialized']

# the -1 index acceses the last element in a list withouth knowing the length
# very useful!

print(bicycles[-1])

# We can use our list elments into a sentace using format
message = "My first bicycle was {}".format(bicycles[0].title())
print( message )

# we can change elements inside a list by  over riding the element as follow:

bicycles[1] = 'yes'
print(bicycles)

# We can use append to add an element to our list
bicycles.append('Tulib')
print(bicycles)
# we can delete an element from our list using del

del bicycles[-1]
print(bicycles)

# Use an item after removing it from a list using pop

poped_item = bicycles.pop()
print(poped_item)
print(bicycles)
bicycles = ['terk','cannodale','redline','specialized']

# You can pop an item from any poisition in the list using the index as follow
first_bicycle = bicycles.pop(0)
print(first_bicycle)


# We can remove an item by using the value of it inside our list :

bicycles.remove('cannodale')
print(bicycles)

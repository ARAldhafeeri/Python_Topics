a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
a.keys() & b.keys() # {'x', 'y'}

# find keys in a but not in b
a.keys() - b.keys()  # {'z'}

# find (key, value) pairs in common
a.items() & b.items() # { ('y', 2) }

# Make a new dictionary with certain keys removed
c = {key : a[key] for key in a.keys() - {'z', 'w'}}
print(c)

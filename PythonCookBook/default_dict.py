from collections import defaultdict


# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

"""
Output:

1
2
Not Present

"""
# regular dict vs defaultdict
d = {'1': 1, '2': 2}
# regular
regular = {}
for key, value in d.items():
    if key not in regular:
        regular[key] = []
    regular[key].append(value)

# defaultdict cleaner code

dd = defaultdict(list)
for key, value in d.items():
    dd[key].append(value)

print(regular['3']) # key error
print(dd['3'])      # []

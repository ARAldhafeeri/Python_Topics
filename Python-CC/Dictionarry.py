alien_0 = {'color': 'green', 'points': 5}
# adding to a dictionary
alien_0['x_position']=10
alien_0['y_position']= 11
print(alien_0)

# modifiying values in a dictionary

alien_0['color'] = 'blue'
print(alien_0)

# deleting a key-value pairs using del

del alien_0['points']
print(alien_0)


# Handling throwbacks error in dictionary using great

#alien_0.get('points','No point value assigned')
#print(alien_0["points"])

# get all the key values inside a dictionary
for value in set(alien_0.values()):
    print(value)

# Get all the keys same method:
for key in set(alien_0.keys()):
    print(key)

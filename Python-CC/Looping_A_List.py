magicians = ['Alice', "david","carolina"]
for magician in magicians:
    print("{} , that was a great tick!".format(magician.title()))
    # Use the next item in the list
    print(f"Can't wait to see your trick!!, {magician.title()}.\n ")

# Using range to construct a list of even numbers

newlist = list(range(2,11,2))
print(newlist)

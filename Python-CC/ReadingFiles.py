with open('pi_digits.txt') as file_object:
    # Reading the whole file:
    contents = file_object.read()
    print(contents)
    # reading line by line:
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    # Turning a file into a list
    lines = file_object.readlines()
    print(lines)
    listme = []
    for line in lines:
        print(line.rstrip())
        listme.append(line.rstrip())

print(listme)

# Remove white spaces: using strip()
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.strip())
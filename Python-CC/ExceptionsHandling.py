try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")


# Using else

a = int(input('enter first number'))
b = int(input('enter second number'))
try:
    answer = a / b
except ZeroDivisionError:
    print(" You can't devided by zero")
else:
    print(answer)


# Handling FileNotFoundError

filename = 'alice.txt'
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print('Cant find file double check the name')

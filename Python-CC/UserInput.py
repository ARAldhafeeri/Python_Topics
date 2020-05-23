# name = input("Please enter your name: ")
# prompt = (f"\n Hello, {name}!")
# print(prompt)

# Here is a better way to write prompt

prompt = " Tell us your name. "
prompt += "\n to personalize a message for you. what is your name? "
name = input(prompt)
print(f"\n Hello, {name}!")

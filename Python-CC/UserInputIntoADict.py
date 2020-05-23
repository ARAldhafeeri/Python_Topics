responses = {}

# set a flag to indicate that poling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\n What is your name ? ")
    response = input("Where do you live ? ")
    # Store our information in our dictionary
    responses[name] = response
    # Maybe more than one trying to input information ?

    repeat = input(" Is there anyone else want to enter thier information ? yes/no ")
    if repeat == "no":
        polling_active = False

print("\n -- poll results --")
for name, response in responses.items():
    print(f"{name}  lives in {response}.")

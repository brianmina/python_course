#
#
# prompt = "\nAdd some toppings to your pizza: "
# prompt += "\n(Enter 'quit' when you finished.)"
#
# while True:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         break
#     else:
#         print(f"Ok, adding {toppings} to your pizza!")
#
#
# prompt = input("How old are you?: ")
# age = int(prompt)
# if age <= 3:
#     print("Your ticket is for free!")
# elif age <= 12:
#     print("Your ticket is $10.")
# else:
#     print("Your ticket is $15.")
#
#
prompt = "\nwhat is your favorite number?: "
prompt += "\n(Enter 'quit' when you finished.)"


number = ""
favorite_number = 20
while True:
    number = input(prompt)
    if number.isnumeric():
        favorite_number = int(number)
    else:
        print("thats not a number")
        break
    if number == 'quit' or favorite_number >= 20:
        break
    else:
        print("I like that number!")


# prompt = "\nfavorite color?: "
# prompt += "\n(Enter 'quit' when you finished.)"
#
# active = True
#
# while True:
#     color = input(prompt)
#     if color == 'quit':
#         break







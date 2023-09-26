

alien_color = "green"
if alien_color == "green":
    print("Great!, you earned 5 points.")
else:
    print("You earned 10 points.")


alien_color = "green"
if alien_color != "green":
    print("Great!, you earned 5 points.")
else:
    print("You earned 10 points.")


players_on = 5
if players_on <= 5:
    print("Good!, ready to play!")
else:
    print("Too many!")


if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == 'yellow':
    print("You earned 10 points.")
elif alien_color == "red":
    print('You earn 15 points.')
else:
    print("You earned 0 points")


age = 65
if age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Elder")


favorite_fruits = ["mango", "peach", "strawberry"]
if "mango" in favorite_fruits:
    print("You really like mango!")
if "peach" in favorite_fruits:
    print("You really like peach!")
if "strawberry" in favorite_fruits:
    print("You really like strawberry!")
if "mango" not in favorite_fruits:
    print("Don't you like mango?")
if "peach" not in favorite_fruits:
    print("Don't you like peach?")
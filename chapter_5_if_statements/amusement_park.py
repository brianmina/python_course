

age = 12
if age < 4:
    print("Your admisision cost is $0.")
elif age < 18:
    print("Yout admission cost is $25.")
else:
    print("Your admission cost is $40.")


admission_age = 40
if admission_age < 4:
    price = 0
elif admission_age < 18:
    price = 25
elif admission_age < 65:
    price = 40
else:
    price = 20
    print(f"Your admission cost is ${price}")

#we can use only 'if' and 'elif' statments

admission_age = 40
if admission_age < 4:
    price = 0
elif admission_age < 18:
    price = 25
elif admission_age < 65:
    price = 40
elif admission_age >= 65:
    price = 20
    print(f"Your admission cost is ${price}")
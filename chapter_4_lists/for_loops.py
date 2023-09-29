

cats = ['gero', 'tony','crista']
for cat in cats:
    print(f'Good job {cat.title()}!')
    print(f'Name of cat: {cat.title()}\n')

print('Thank you cats!')


pizzas = ['hawaiian', 'peperoni','mexican']
friends_pizzas = pizzas[:]

pizzas.append("tropical")
friends_pizzas.append("cheese")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizza are:")

for friends_pizza in friends_pizzas:
    print(friends_pizza)

print('I really love pizza!')

animals = ['tiger','leon', 'babydog']
for animal in animals:
    print(f'A {animal.title()} would be a great pet!.')
print('Any of these animals would make a great pet.')

print(f'The frist two animals are:')
print(animals[0:2])

print(f'Two last animals od the list are: {animals[1:3]}')
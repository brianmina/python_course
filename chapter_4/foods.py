players = ['mario', 'peach', 'luigi', 'toad']
print('The winners are:')
for player in players[0:3]:
    print(player.title())

my_food = ['pizza','falafel','carrot cake']
friends_food = my_food[:]

my_food.append('cannoli')
friends_food.append('ice crema')

print('My favorite for are:')
print(my_food)

print("\nMy friends's favoritve food are:")
print(friends_food)

for food in my_food:
    print(food)
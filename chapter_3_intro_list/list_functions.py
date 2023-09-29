
anything = ['dog','cat','burger','fries','soda','hawaii',17,18,'colombia','green']
print(f'Original list: \n{anything}')

print(f'Accesing to the number 0 element: {anything[0].title()}')
print(f'Index positions -1 and 4: {anything[-1].title()}, {anything[4].title()}')

my_country = anything[-2]
print(f'I was born in: {my_country.title()}!')

anything[8] = 'usa'
print(f'I live in: {anything[9].title()}!')

anything.append("colombia")
print(f"But I'll visit to {anything[10].title()} with my husband :).")
print(anything)

anything.insert(0,"chicken")
print(f'Favorite food: {anything[0].title()}')

del anything[11]
print(anything)

favorite_color = anything.pop()
print(f'I like: {favorite_color.title()} color!')

unhealthy_food = anything.pop(4)
print(f'Try to avoid: {unhealthy_food.title()}!')

anything.remove("soda")
print(anything)

anything.remove(17)
anything.remove(18)
print(anything)

anything.sort()
print(anything)

anything.sort(reverse=True)
print(anything)

print(sorted(anything))
print(sorted(anything,reverse=True))

anything.reverse()
print(anything)

print(len(anything))

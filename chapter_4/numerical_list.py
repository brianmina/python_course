numbers = list(range(2,11,2))
print(numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# more concisely

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

days = [value**2 for value in range(1,11)]
print(days)


for numbers in range(1,21):
    print(numbers)

millions = []
for digits in range(1,1000001):
    millions.append(digits)
print(min(millions))
print(max(millions))
print(sum(millions))

odd = []
for number in range(0,21,3):
    odd.append((number))
print(odd)

threes = []
for three in range(3,31,3):
    threes.append(three)
print(threes)

# using expressions
cubes= []
for cube in range(1,11):
    value = cube**3
    cubes.append(value)
print(cubes)


# list comprehension
new_cube = [cube**3 for cube in range(1,11)]
print(new_cube[0:11:5])



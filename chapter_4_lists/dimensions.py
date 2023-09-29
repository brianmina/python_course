dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# a tuple never can be changed /ERROR/
#dimensions[0] = 250

my_t = (3,)

for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions')
for dimension in dimensions:

    print(dimension)


person = {
    'first_name': 'brian',
    'last_name': 'mina',
    'age': '29',
    'city': 'oakland Park'
}
fist_name = person['first_name'].title()
last_name = person['last_name'].title()
age = person['age']
city = person['city'].title()

print(f"Name: {fist_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"Current city: {city}")


favorite_numbers = {
    'brian': '17',
    'karl': '9',
    'Helen': '15',
    'jorge': '25',
    'cooper': '1'
}

print(f"Brian's favorite number is: {favorite_numbers['brian'].title()}")
print(f"Karl's favorite number is: {favorite_numbers['karl'].title()}")
print(f"Helen's favorite number is: {favorite_numbers['Helen'].title()}")
print(f"Jorge's favorite number is: {favorite_numbers['jorge'].title()}")
print(f"Cooper's favorite number is: {favorite_numbers['cooper'].title()}")


new_words = {
    'indentation': 'spaces, lines, or block to write a clean code.',
    'syntax': 'the arrangement of word and phrases to create sentences in a language.',
    'exception': 'it is a error.',
    'argument': 'information of a function.',
    'loop': 'an element that repeat a portion of code.',
    'set': 'a list of a dictionary with unique elements.'
}
for key, value in new_words.items():
    print(f"\nWord: {key}")
    print(f"Meaning: {value}")

rivers = {
    'nile': 'egypt',
    'amazon': 'colombia',
    'yangtze': 'china',
}
for river, country in rivers.items():
  print(f"The {river.title()} runs through {country.title()} ")
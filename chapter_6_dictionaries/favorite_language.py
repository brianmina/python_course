

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_language['sarah'].title()
print(f"sarah's favorite language is {language}")

# ask for a key that doesn't exist
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points')
print(point_value)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
 #   print(f"Hi {name.title()}")

  #  if name in friends:
   #     language = favorite_languages[name].title()
    #    print(f"\t{name.title()} I see you love {language}")


pending = ['phil', 'sarah']
for names in favorite_languages.keys():
    print(f"Hi {names.title()} !")

    if names in pending:
        should = favorite_languages[names].title()
        print(f"\t{names} please take the poll.")
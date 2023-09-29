

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

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)



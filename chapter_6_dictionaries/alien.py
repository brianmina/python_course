

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
# add key value pairs to the dictionary.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_1 = {}
alien_1["color"] = "green"
alien_1["points"] = 5
print(f"The alien is {alien_1['color']}.")
alien_1['color'] = "yellow"
print(f"The alienis now {alien_1['color']}.")
print(alien_1)


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'

# Move the alien t the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3


# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

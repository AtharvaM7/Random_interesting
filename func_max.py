'''We have a function in two variables. We need to find a point where the
function has a maximum value.'''

def math_func(x, y):
    '''This function is the function we need to maximize.'''
    return -(x-1)**2 - y**2 + 1

def max_func():
    '''This function starts with a value of 0 for each variable.
    Then we randomly change the value of all variables and compare it with the previous value.
    If the new value is greater than the previous one, we keep it, else we move
    in the opposite direction.'''
    import random
    import math
    # We change x and y randomly by + or - 0.0001
    eps = 0.0001
    # Create a variable to store the maximum value of the function
    max_value = 0
    # Start with x, y = 0,0 and append the value to the max_value
    x=0
    y=0
    max_value = math_func(x, y)
    # Keep going in some random direction till our function stops increasing
    while max_value < math_func(x,y):
        # Change x and y randomly by + or - 0.0001
        x = x + random.choice([-eps, eps])
        y = y + random.choice([-eps, eps])
        # If the new value is greater than the previous one, we keep it, else we move
        # in the opposite direction.
        if math_func(x,y) > max_value:
            max_value = math_func(x,y)
        else:
            x = x - random.choice([-eps, eps])
            y = y - random.choice([-eps, eps])
    return max_value
# Call the function
print(max_func())

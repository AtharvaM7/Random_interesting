# write a code to find maximum value of a function in two variables x,y

import random
import math


def f(x,y):
    return math.sqrt(2025-(x**2 + y**2))

# defining variables
x,y=0,0
eps=1*random.randint(-10,10)
delta=1*random.randint(-10,10)

for i in range(1):
    if f(x+eps,y+delta)>f(x,y):
        x=x+eps
        y=y+delta
    else:
        eps=-eps
        delta=-delta

print("Maximum value of the function is: ",f(x,y))

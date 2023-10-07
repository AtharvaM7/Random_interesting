#simulate a selection of 10 numbers from a sample of 100 numbers.

import random
import numpy as np
import matplotlib.pyplot as plt

#assign percentile to the population
population = []
percentile = [0]*10000

for i in range(100000):
    population.append(random.sample(range(1,100001),100000))
    
#select 100 people from the population
sample = random.sample(population,100)
sample_percentile = [0]*100

for i in range(100):
    sample_percentile[i]=((sample[i])/100000*100)

print (sample_percentile)


#simulate a selection of 10 numbers from a sample of 100 numbers.

import random
import numpy as np
import matplotlib.pyplot as plt

#assign percentile to the population
population = []
percentile = [0]*100000

for i in range(1000000):
    population.append(random.sample(range(1,1000001),1000000))
    
#select 100 people from the population
sample = random.sample(population,100)
sample_percentile = [0]*100

for i in range(100):
    sample_percentile[i]=((sample[i])/1000000*100)

print (sample_percentile)


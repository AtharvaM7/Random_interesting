'''To prove that on an average, if we take a random number in an unsorted
list, it will lie outside the first and last quarter of the sorted list'''

'''Hence proving that on an average we can cut off 25% of the list'''
import random
import matplotlib.pyplot as plt

#create a list of 100 random numbers
list = []
for i in range(10000):
    list.append(random.random())

#sort the list
sorted_list = list
sorted_list.sort()

#take a random number from the list and find its index in the sorted list and
#then appending the index to a new list of indices

indices = []
for i in range(100000):
    indices.append(sorted_list.index(random.choice(list)))

#calculating the average of the indices
average = sum(indices)/len(indices)

print(average)


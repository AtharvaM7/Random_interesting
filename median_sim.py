#Simulating and answering why on an average, we cut down 25% of the list while
#finding median rom an unsorted list without sorting.

import random

#create a list with 10000 random numbers
list = []
for i in range(10000):
    list.append(random.random()) #adds random numbers to the list

#we create a sorted version of the list to compute the number of elements that
#are cut down while finding the median
sorted_list = list
sorted_list.sort()


#now we randomly select an element from the list and check its index in the
#sorted list

#no. of elements cut down = total no. of elements - index of the element in
#the sorted list - 1

#we repeat this process 1000 times and find the average of the no. of elements

cut_down = []
for i in range(1000):
    #selects a random element
    element = random.choice(list)

    #gives us index of the element in the sorted list
    index = sorted_list.index(element)
    
    if index>=5000:
        cut_down.append(10000-index-1)
    else:
        cut_down.append(index)

#average of the no. of elements cut down
avg = sum(cut_down)/len(cut_down)
print(avg)

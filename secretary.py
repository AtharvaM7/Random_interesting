#Take input n from user.
n = int(input("Enter n: "))

#Create a list with elements 1 to n and shuffle it randomly
import random
l = list(range(1,n+1))
random.shuffle(l)

k= n*0.36787944117144233
k = int(k)

#find the maximum of the first k elements of the shuffled list
maximum = max(l[:k])

#Go through rest of the list and find the first number that is greater than 
#the maximum of the first k elements. If no such number exists, then the
#return the last number of the shuffled list
def secretary(l,maximum):
    for i in range(k,n):
        if l[i] > maximum:
            return l[i]
    return l[n-1]

#plot histogram of the outputs of the secretary function for 1000 trials with a
#lot of bins
#import matplotlib.pyplot as plt
#l2 = []
#for i in range(10000):
#    l = list(range(1,n+1))
#    random.shuffle(l)
#    maximum = max(l[:k])
#    l2.append(secretary(l,maximum))
#
#plt.hist(l2,bins=100)
#plt.show()

#find average of the outputs of the secretary function for 1000000 trials
l2 = []
for i in range(10000):
    l = list(range(1,n+1))
    random.shuffle(l)
    maximum = max(l[:k])
    l2.append(secretary(l,maximum))

print(sum(l2)/len(l2))


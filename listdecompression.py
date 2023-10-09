'''This program takes a compressed image which is expressed in the form of list
of tuples and comverts it back to the original image.'''

# Take the input of location of the compressed image from the user
location = input("Enter the location of the compressed image: ")

# Open the file. Each line of the file is a tuple. Create a list of those
# tuples.
f=open(location,"r")
compressed_image = []
for line in f:
    # Remove the brackets and split the line into a tuple of integers
    line = line.replace("(","")
    line = line.replace(")","")
    line = line.split(",")
    line = tuple(map(int,line))
    # Append the tuple to the list
    compressed_image.append(line)
f.close()

# Now we have a list of tuples. First element of each tuple denotes the pixel
# value and the second element denotes the number of times it is repeated.
# We need to turn this list of tuples back to the list of pixel values.

def decompress(l):
    '''This function takes a list of tuples and returns the original image
    array.'''
    # Create an empty list
    decompressed_image = []
    # For each tuple in the list, append the first element of the tuple to the
    # list as many times as the second element of the tuple.
    for i in l:
        decompressed_image.extend([i[0]]*i[1])
    return decompressed_image

# Convert the list of pixel values back into an image and display it
import numpy as np
import math
import matplotlib.pyplot as plt
decompressed_image = np.array(decompress(compressed_image))
decompressed_image = decompressed_image.reshape(int(math.sqrt(len(decompressed_image))),int(math.sqrt(len(decompressed_image))))
plt.imshow(decompressed_image,cmap="gray")
plt.show()



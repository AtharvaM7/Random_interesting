'''Open the image mrdog.jpg in the current directory.
Conbert it to grayscale.
Convert the image into a numpy array.
Print the arrays.
'''

import numpy as np
from PIL import Image
import random

# Open the image and convert it to grayscale
image = Image.open('mrdog.jpg').convert('L')

# Convert the image into a numpy array
image_array = np.array(image)

# Print the image and the array
print(image)
print(image_array.shape)

# duplicate the matrix
image_array2 = image_array.copy()

# Find a pixel randomly and output the row and column in the numpy array
row = np.random.randint(0, image_array.shape[0])
col = np.random.randint(0, image_array.shape[1])
    

# Print the pixel value
print(image_array[row, col])

# Change the pixel value to 0
image_array[row, col] = 0



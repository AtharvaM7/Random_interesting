'''This program takes an image important.png and converts it to numpy array.
Then it saves the numpy array as a text file.'''
import numpy as np
from PIL import Image

# Load image:
img = Image.open('important_af.png')

# Convert image into a 2D numpy array:
arr = np.array(img)

# Save the numpy array as a text file:
np.savetxt('important.txt', arr, fmt='%d')



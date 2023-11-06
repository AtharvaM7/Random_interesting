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

''' 
The i,j entry of the matrix is the pixel value at row i and column j which is
deleted by the above code.
Swap the ith row with the last row.
Swap the jth column with the last column.
Create a new matrix A with the last column deleted.
A is a rectangular matrix.
Express the last row of A as a linear combination of the other rows.
Find the coefficients of the linear combination using least squares method.
Multiply the last columns of the original matrix by the coefficients and print the
result.
'''
# Uncomment the following code to see the result

############################# ROW-WISE #########################################

## Swap the ith row with the last row
#image_array2[[row, image_array2.shape[0]-1]] = image_array2[[image_array2.shape[0]-1, row]]

## Swap the jth column with the last column
#image_array2[:, [col, image_array2.shape[1]-1]] = image_array2[:, [image_array2.shape[1]-1, col]]

## Create a new matrix A with the last row deleted
#A = image_array2[:-1, :-1]

## Express the last column of A as a linear combination of the other columns
## Find the coefficients of the linear combination using least squares method
#coeff = np.linalg.lstsq(A, image_array2[:-1, -1], rcond=None)[0]

## Multiply the last row of the original matrix by the coefficients and print the result
#print(np.dot(coeff, image_array2[-1, :-1]))

############################## COLUMN-WISE ######################################

## Swap the ith row with the last row
#image_array2[[row, image_array2.shape[0]-1]] = image_array2[[image_array2.shape[0]-1, row]]

## Swap the jth column with the last column
#image_array2[:, [col, image_array2.shape[1]-1]] = image_array2[:, [image_array2.shape[1]-1, col]]

##Create a new matrix A with the last row deleted
#A = image_array2[:-1, :-1]

## Express the last column of A as a linear combination of the other columns
## Find the coefficients of the linear combination using least squares method
#coeff = np.linalg.lstsq(A, image_array2[:-1, -1], rcond=None)[0]

## Multiply the last row of the original matrix by the coefficients and print the result
#print(np.dot(coeff, image_array2[-1, :-1]))


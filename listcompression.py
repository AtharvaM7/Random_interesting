'''This is a program that compresses an image using the concept of hilbert's
space filling curve.'''
import numpy as np


# write a function that takes a list and writes the consecutive repeated
# elements as a tuple of the form (element, number of repetitions)

def compress_list(l):
    '''This function takes a list and writes the consecutive repeated elements
    as a tuple of the form (element, number of repetitions).'''
    # initialize variables
    compressed_list = []
    count = 1
    # loop through the list
    for i in range(len(l)):
        # if the element is the last element in the list
        if i == len(l) - 1:
            # append the element and the number of repetitions to the list
            compressed_list.append((l[i], count))
        # if the element is not the last element in the list
        else:
            # if the element is the same as the next element
            if l[i] == l[i + 1]:
                # increment the count
                count += 1
            # if the element is not the same as the next element
            else:
                # append the element and the number of repetitions to the list
                compressed_list.append((l[i], count))
                # reset the count
                count = 1
    # return the compressed list
    return compressed_list

# write a function that opens an image, converts it into greyscale, makes it a
# square and then converts it into a numpy array

def open_image(filename):
    '''This function opens an image, converts it into greyscale, makes it a
    square and then converts it into a numpy array.'''
    # import the necessary libraries
    from PIL import Image
    import numpy as np
    # open the image
    image = Image.open(filename)
    # convert the image into greyscale
    image = image.convert('L')
    # make the image a square
    image = image.resize((256, 256))
    # convert the image into a numpy array
    image = np.array(image)
    # return the image
    return image

#__________________________________________________________________________________________________________________________________________________________________________________________________________#_

# Code that follows gives us the coordinates that we need to parse through the
# array in the order of the space filling curve

def input_n():
    '''This function takes the input of n from the user'''
    #Take input
    n=int(input('Enter the number: '))
    return n

#create initial figure
in_fig=('d','r','u')

def rot_cw(list):
    '''This funcion takes a string of ruld moves and rotates it clockwise'''
    for i in range(len(list)):
        #On rotating right becomes up, down becomes left, left becomes down and up becomes right
        if list[i]=='r':#exchange r with u
            list[i]='u'
        elif list[i]=='d':#exchange d with l
            list[i]='l'
        elif list[i]=='l':#exchange l with d
            list[i]='d'
        else:
            list[i]='r'#exchange u with r
    return list

def rot_ccw(list):
    '''This function takes a list of ruld moves and rotates it counter clockwise'''
    for i in range(len(list)):
        #On ratating right becomes down, up becomes left, left becomes up, down becomes right
        if list[i]=='r':#exchnge r with u
            list[i]='d'
        elif list[i]=='u':#exchange u eith l
            list[i]='l'
        elif list[i]=='l':#exchage l with d
            list[i]='u'
        else:
            list[i]='r'#exchnge d with r

    return list

def fig_co(list):
    '''This function takes a list of ruld moves and converts it to coordinates such that we start from 1,1'''
    #Defining a list to store tuples of (x,y)
    store=[]
    #define x and y coordinates
    x=0
    y=0
    #update the initial position
    store.append((y,x))
    #x increases whe we go to right and decreasesw when we go to left
    #y increases when we go down and decreases when we go up
    for i in range(len(list)):
        if list[i]=='r':
            x=x+1
        elif list[i]=='l':
            x=x-1
        elif list[i]=='d':
            y=y+1
        elif list[i]=='u':
            y=y-1
        store.append((y,x))
    return store

def fig(n):
    '''This function takes the input n from the user and creates the sfc figure by joining the four quarters'''
    if n==1:
        moves=list(in_fig)
        return moves
    else:
        figure=tuple(fig(n-1))
        #Create a variable to store the list of moves
        moves=[]
        #create local variables
        temp1=rot_ccw(list(figure))
        temp2=list(figure)
        temp3=list(figure)
        temp4=rot_cw(list(figure))
        p=len(figure)

        #Top left
        for i in range(p):
            moves.append(temp1[i])
        #Connect top left and bottom left
        moves.append('d')
        #bottom left
        for i in range(p):
            moves.append(temp2[i])
        #connecting bottom left and bottom right
        moves.append('r')
        #bottom right
        for i in range(p):
            moves.append(temp3[i])
        #conneting bottom right and top right
        moves.append('u')
        #top right
        for i in range(p):
            moves.append(temp4[i])

    return moves

def SFC(n):
    return fig_co(fig(n))
#__________________________________________________________________________________________________________________________________________________________________________________________________________#


# Now we parse the numpy array in the order of the space filling curve and
# create a list of the pixel values

def parse_array(image):
    '''This function parses the numpy array in the order of the space filling
    curve and creates a list of the pixel values.'''
    # initialize variables
    parsed_array = []
    # get the coordinates of the space filling curve
    # coordinates will be the log base 2 of the length of the array
    coordinates = SFC(int(np.log2(len(image))))
    # go through all the coordinates
    for i in range(len(coordinates)):
        # append the pixel value to the list
        parsed_array.append(image[coordinates[i][0]][coordinates[i][1]])
    # return the parsed array
    return parsed_array


def main():
    '''This is the main function.'''
    # take image path input from the user
    image_path = input('Enter the path of the image: ')
    # open the image
    image = open_image(image_path)
    # parse the array
    parsed_array = parse_array(image)
    # compress the list
    compressed_list = compress_list(parsed_array)
    # print the compressed list
    print(compressed_list)

main()

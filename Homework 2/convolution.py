import numpy as np
import cv2

#input image as provided by question
img = cv2.imread('/Users/akankshabhattacharyya/Downloads/SEM1 Courses/DIS/anbhatta_hw02/DSC_0745.JPG')
gray = img[:,:,0]

#tested on sobel x operator
sobel = [[-1,-2,-1],
         [0, 0, 0],
         [1, 2, 1]]
#tested on laplacian operator
laplacian = [[0,-1,0],
             [-1,4,-1],
             [0,-1,0]]

#convolution function, takes argument as image and filter(sobel/laplacian)
def convolution(gray,filter):
    A = np.pad(gray,(1,1),'constant')
    conv = np.zeros((len(gray),len(gray[0])))

    for row in range(0,len(gray)):
        for col in range(0,len(gray[0])):
            sum1 = A[row][col] * filter[0][0] + A[row][col + 1] * filter[0][1] + A[row][col + 2] * filter[0][2] + \
                   A[row + 1][col] * filter[1][0] + A[row + 1][col + 1] * filter[1][1] + A[row + 1][col + 2] * \
                   filter[1][2] + \
                   A[row + 2][col] * filter[2][0] + A[row + 2][col + 1] * filter[2][1] + A[row + 2][col + 2] * \
                   filter[2][2]
            conv[row][col] = sum1
            col += 1
        row += 1
    return conv


#display shape option : full/same/valid after convolution
def shape_option(img,shape):
    if shape == 'full':
        return img
    elif shape == 'same':
        img = img[2:len(conv)-2][2:len(img[0])-2]
        return img
    elif shape == 'valid':
        img = img[4:len(conv)-4][4:len(img[0])-4]
        return img


#to take input from user on the type of convolution and output shape type
filter = input("Enter convolution filter type : laplacian or sobel ")
shape = input("enter shape option: full, same or valid ")

if filter == 'laplacian':
    conv = convolution(gray, laplacian)
    if shape == 'full':
        output = shape_option(conv, 'same')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape == 'same':
        output = shape_option(conv,'same')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape == 'valid':
        output = shape_option(conv,'valid')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("enter again")

elif filter == 'sobel':
    conv = convolution(gray, sobel)
    if shape == 'full':
        output = shape_option(conv, 'same')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape == 'same':
        output = shape_option(conv, 'same')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape == 'valid':
        output = shape_option(conv, 'valid')
        cv2.imshow('image', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("enter again")
else:
    print("enter valid filter")







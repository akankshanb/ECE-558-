import numpy as np
import cv2

#input image as provided in question
img = cv2.imread('/Users/akankshabhattacharyya/Downloads/SEM1 Courses/DIS/HW02-Due10-03/lena-gray.bmp')
gray = img[:,:,0]

#clip_padding function
def clip_filter(gray):
    A = np.pad(gray,(20,20),'constant')
    return A

#copy_edge function
def copy_edge(gray):
    indxa = 1
    num_dups = 20
    gray = np.insert(gray,[indxa+1]*num_dups,gray[indxa],axis=0)
    indxb = len(gray)-1
    gray = np.insert(gray,[indxb+1]*num_dups,gray[indxb],axis=0)

    indxc = len(gray[0]) - 1
    gray = np.insert(gray,[indxc+1]*num_dups,gray[:,[indxc]],axis=1)
    gray = np.insert(gray,[indxa+1]*num_dups,gray[:,[indxa]],axis=1)
    return(gray)

#reflect function
def reflect(gray):
    for i in range(0,20):
        gray = np.insert(gray,0,gray[0+2*i],axis=0)
        gray = np.insert(gray,len(gray)-1,gray[len(gray)-1-2*i],axis=0)
    for j in range(0,20):
        gray = np.insert(gray,0,gray[:,0+2*j],axis=1)
        gray = np.insert(gray,len(gray[0])-1,gray[:,len(gray[0])-1-2*j],axis=1)
    return gray

#wrap_around function
def wrap_around(gray):
    test = np.copy(gray)
    for col in range(0,20):
        for row in range(0,len(test)):
            test[row][len(test[0])-1-col] = gray[row][col]
            test[row][col] = gray[row][len(test[0])-1-col]
    for row in range(0,20):
        for col in range(0,len(test[0])):
            test[len(test)-1-row][col] = gray[row][col]
            test[row][col] = gray[len(gray)-1-row][col]
    return test

#takes input from user about padding option
pad_option = input("Enter padding option : clip, edgecopy, reflect or wrap  ")

if pad_option == 'clip':
    clip = clip_filter(gray)
    cv2.imshow('image',clip)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif pad_option == 'edgecopy':
    copy = copy_edge(gray)
    cv2.imshow('image',copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif pad_option == 'reflect':
    ref = reflect(gray)
    cv2.imshow('image',ref)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif pad_option == 'wrap':
    wrap = wrap_around(gray)
    cv2.imshow('image', wrap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import numpy as np
import cv2
from collections import OrderedDict

# from PIL import Image
# from scipy import misc

s = 'anbhatta'
l = [ord(c) for c in s]
print(l)

img = cv2.imread('..path/wolves.png')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

red = img[:, :, 2]
blue = img[:, :, 1]
green = img[:, :, 0]

red_list = red.flatten()
r_l = red_list.tolist()

green_list = blue.flatten()
g_l = green_list.tolist()

blue_list = green.flatten()
b_l = blue_list.tolist()

l1 = list(OrderedDict.fromkeys(l))
print(l1)
count = 0
count1 = 0
count2 = 0
for i in l1:
    for j in r_l:
        if i == j:
            count += 1
    print(str(i) + ' in red: ' + str(count))
    count = 0
for i in l1:
    for j in b_l:
        if i == j:
            count1 += 1
    print(str(i) + ' in blue: ' + str(count1))
    count1 = 0
for i in l1:
    for j in g_l:
        if i == j:
            count2 += 1
    print(str(i) + ' in green: ' + str(count2))
    count2 = 0

red = np.pad(red, (2, 2), 'constant')
green = np.pad(green, (2, 2), 'constant')
blue = np.pad(blue, (2, 2), 'constant')

for i in range(len(red)):
    for j in range(len(red[0, :])):
        if red[i][j] == 97:
            red[i][j] = red[i - 2][j - 2] = red[i + 2][j + 2] = red[i + 2][j - 2] = red[i - 2][j + 2] = red[i][j + 2] = \
            red[i][j - 2] = red[i - 2][j] = red[i + 2][j] = 255
        elif red[i][j] == 110:
            red[i][j] = red[i - 2][j - 2] = red[i + 2][j + 2] = red[i + 2][j - 2] = red[i - 2][j + 2] = red[i][j + 2] = \
            red[i][j - 2] = red[i - 2][j] = red[i + 2][j] = 255
        elif red[i][j] == 98:
            red[i][j] = red[i - 2][j - 2] = red[i + 2][j + 2] = red[i + 2][j - 2] = red[i - 2][j + 2] = red[i][j + 2] = \
            red[i][j - 2] = red[i - 2][j] = red[i + 2][j] = 255
        elif red[i][j] == 104:
            red[i][j] = red[i - 2][j - 2] = red[i + 2][j + 2] = red[i + 2][j - 2] = red[i - 2][j + 2] = red[i][j + 2] = \
            red[i][j - 2] = red[i - 2][j] = red[i + 2][j] = 255
        elif red[i][j] == 116:
            red[i][j] = red[i - 2][j - 2] = red[i + 2][j + 2] = red[i + 2][j - 2] = red[i - 2][j + 2] = red[i][j + 2] = \
            red[i][j - 2] = red[i - 2][j] = red[i + 2][j] = 255
        else:
            red[i][j] = red[i][j]

for i in range(len(green)):
    for j in range(len(green[0, :])):
        if green[i][j] == 97:
            green[i][j] = green[i - 2][j - 2] = green[i + 2][j + 2] = green[i + 2][j - 2] = green[i - 2][j + 2] = \
            green[i][j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif green[i][j] == 110:
            green[i][j] = green[i - 2][j - 2] = green[i + 2][j + 2] = green[i + 2][j - 2] = green[i - 2][j + 2] = \
            green[i][j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif green[i][j] == 98:
            green[i][j] = green[i - 2][j - 2] = green[i + 2][j + 2] = green[i + 2][j - 2] = green[i - 2][j + 2] = \
            green[i][j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif green[i][j] == 104:
            green[i][j] = green[i - 2][j - 2] = green[i + 2][j + 2] = green[i + 2][j - 2] = green[i - 2][j + 2] = \
            green[i][j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif green[i][j] == 116:
            green[i][j] = green[i - 2][j - 2] = green[i + 2][j + 2] = green[i + 2][j - 2] = green[i - 2][j + 2] = \
            green[i][j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        else:
            green[i][j] = green[i][j]

for i in range(len(blue)):
    for j in range(len(blue[0, :])):
        if blue[i][j] == 97:
            blue[i][j] = blue[i - 2][j - 2] = blue[i + 2][j + 2] = blue[i + 2][j - 2] = blue[i - 2][j + 2] = green[i][
                j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif blue[i][j] == 110:
            blue[i][j] = blue[i - 2][j - 2] = blue[i + 2][j + 2] = blue[i + 2][j - 2] = blue[i - 2][j + 2] = green[i][
                j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif red[i][j] == 98:
            blue[i][j] = blue[i - 2][j - 2] = blue[i + 2][j + 2] = blue[i + 2][j - 2] = blue[i - 2][j + 2] = green[i][
                j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif blue[i][j] == 104:
            blue[i][j] = blue[i - 2][j - 2] = blue[i + 2][j + 2] = blue[i + 2][j - 2] = blue[i - 2][j + 2] = green[i][
                j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        elif blue[i][j] == 116:
            blue[i][j] = blue[i - 2][j - 2] = blue[i + 2][j + 2] = blue[i + 2][j - 2] = blue[i - 2][j + 2] = green[i][
                j + 2] = green[i][j - 2] = green[i - 2][j] = green[i + 2][j] = 255
        else:
            blue[i][j] = blue[i][j]

# print(green)
# print(red)
# print(blue)

red = red[2:len(red) - 2, 2:len(red[0, :]) - 2]
green = green[2:len(green) - 2, 2:len(green[0, :]) - 2]
blue = blue[2:len(blue) - 2, 2:len(blue[0, :]) - 2]

for i in range(len(blue[:, 0])):
    for j in range(len(blue[0, :])):
        img[i][j][0] = blue[i][j]

for i in range(len(green)):
    for j in range(len(green[0, :])):
        img[i][j][1] = green[i][j]

for i in range(len(red)):
    for j in range(len(red[0, :])):
        img[i][j][2] = red[i][j]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
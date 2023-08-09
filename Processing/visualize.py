# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 00:36:20 2022

@author: Asus
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

xx = []
yy = []

def click_event(event,x,y,a,b):
    if event == cv.EVENT_LBUTTONDOWN:
        xx.append(x)
        yy.append(y)

path = 'F:/captures/4th year thesis/datasets/Sign language/imposed/Frames/1017.jpg'

img = cv.imread(path)

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.imshow(img,'gray')

plt.show()

# print(img.shape)

cv.imshow('image',img)

cv.setMouseCallback('image', click_event)

cv.waitKey(0)

cv.destroyAllWindows()

# print(xx)
# print(yy)



data16 = np.load('F:/captures/4th year thesis/datasets/Sign language/imposed/Points/1016.npy')

data17 = np.load('F:/captures/4th year thesis/datasets/Sign language/imposed/Points/1017.npy')

data18 = np.load('F:/captures/4th year thesis/datasets/Sign language/imposed/Points/1018.npy')


# print(data16[100])

# print(type(data17))

datan=data16.copy()

# # for i in range(126):
# #     datan[i]=0

# print(data17)
# print(data18)

for i in range(126):
    # print(data17[i])
    if(data17[i]==-1.0):
        # print("Hello ",i)
        datan[i] = (data16[i]+data18[i])/2.0
        # print(data17[i])
    else:
        datan[i]=data17[i]
    # if data17[i]==-1.0:
    #     data17[i] = (data16[i]+data18[i])/2.0
    #     print("Wrong")
        
print('16th frame 101st point:',' ',data16[100])
# # print(data17.shape)
# print(datan[100])
# print(data18[100])
print('18th frame 101st point:',' ',data18[100])

print('17th frame 101st point:',' ',data17[100])

print('Average of 101st point:',' ',datan[100])



palm = cv.circle(img, (xx[0],yy[0]), 20, (0,255,0), 10)

plt.imshow(palm,'gray')

plt.show()

# print(datan[67])
# print(datan[68])

id = 63

while 1:
    if id==126:
        break
    

    x_c = xx[0]-116*datan[id]
    y_c = yy[0]-108*datan[id+1]
    
    x_c = np.round(x_c)
    y_c = np.round(y_c)
    
    print(x_c,' ',y_c)
    # print(y_c)
    
    palm = cv.circle(img, (int(x_c),int(y_c)), 60, (255,255,255), 10)
    id=id+3

    plt.imshow(palm,'gray')
    
    plt.show()
cv.imwrite('F:/captures/4th year thesis/datasets/Sign language/imposed/output.jpg',palm)
# plt.show()

# cv2.circle(image, center_coordinates, radius, color, thickness)
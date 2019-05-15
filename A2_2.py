# Nate Brune
# 2/4/2019
# I have not given or received any unauthorized assistance on this assignment. 

import math
import random

def inputCoord(str):
    '''Asks for an input of coordinates, converts it to a list and returns the list'''
    coord = input("Enter the position for "+str+" (format x y): ")
    res = []
    for n in coord.split():
        res.append(int(n))
    return res

def boundingBox(f1, f2, axisLen):
    '''
    takes the two focal points and axis length of the ellipses as input
    calculates the bounding box and returns an dictionary containing the leftBound, rightBound, lowerBound, upperBound
    '''
    minX, maxX = min(f1[0],f2[0]), max(f1[0],f2[0])
    minY, maxY = min(f1[1],f2[1]), max(f1[1],f2[1])
    leftBound, rightBound = (maxX - axisLen), (minX + axisLen)
    lowerBound, upperBound = (maxY - axisLen), (minY +axisLen)
    resultBox = {'leftBound': leftBound, 'rightBound': rightBound, 'lowerBound': lowerBound, 'upperBound': upperBound}
    return resultBox

def interceptPoint(f1, f2, randomPoint):
    '''
    takes in two focal points and randomly generated point as input
    calculates the line that is perpendicular to the major azis and passes through the randomPoint
    returns the point where the perpendicular line and the major axis meets
    this point will be used to calculate the distance from focal points to the random point
    '''
    x1, y1 = f1[0], f1[1]
    x2, y2 = f2[0], f2[1]
    xR, yR = randomPoint[0], randomPoint[1]
    
    m1 = (y2-y1)/(x2-x1)
    b1 = y1-(m1*x1)
    m2 = -1/m1
    b2 = yR-(m2*xR)
    
    resultX = (b1-b2)/(m2-m1)
    resultY = m1+resultX + b1
    result = [resultX, resultY]
    return result

def distToFocalPoint(focalPoint, interceptPoint, randomPoint):
    '''
    takes focalPoint, interceptPoint, and randomPoint coordinates as input
    returns the distance from randomPoint to focalPoint
    '''
    xf, yf = focalPoint[0], focalPoint[1]
    xi, yi = interceptPoint[0], interceptPoint[1]
    xr, yr = randomPoint[0], randomPoint[1]
    d1 = math.sqrt((xr-xi)**2 + (yr-yi)**2)
    d2 = math.sqrt((xf-xi)**2 + (yf-yi)**2)
    result = math.sqrt(d1**2 + d2**2) 
    return result

#gather variables needed to calculate area of an ellipses through inputs
f1 = inputCoord("f1")
f2 = inputCoord("f2")
axisLen = int(input("Enter the length of the major axis (format: 1): "))
nPoints = int(input("Enter the number of random points (format: n): "))

#calculate the bounding box
box = boundingBox(f1,f2,axisLen)

#generate a list containing random points inside the bounding box
randomPointList = []
for x in range(nPoints):
    point = []
    point.append(random.uniform(box['leftBound'],box['rightBound'] + 1))
    point.append(random.uniform(box['lowerBound'],box['upperBound'] + 1))
    randomPointList.append(point)

#for each point in the random list use defined functions to determine if it is in the ellipses
#if it is in the ellipses then increase the counter by 1
inEllipse = 0
for point in randomPointList:
    i = interceptPoint(f1, f2, point)
    d1 = distToFocalPoint(f1, i, point)
    d2 = distToFocalPoint(f2, i, point)
    if d1 + d2 < axisLen:
        inEllipse += 1

#multiply the percentage of random points in the ellipses to the area of the box to get the area of the ellipses
boxArea = (box['rightBound'] - box['leftBound']) * (box['upperBound'] - box['lowerBound'])
ellipseArea = (inEllipse/nPoints)*(boxArea)
print(ellipseArea)
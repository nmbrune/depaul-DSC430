# Nate Brune
# 1/22/2019 
# I have not given or received any unauthorized assistance on this assignment


def overlap(a,b):
    '''calculates the area of overlap between two squares
    the function expects two lists, each containing 3 integers, as input'''
    
    #if there is no overlap on either the x or the y axis then the result is zero
    if min((a[0] + a[2]),(b[0] + b[2])) < max(a[0],b[0]) or min((a[1] + a[2]),(b[1] + b[2])) < max(a[1],b[1]):
        result = 0
    #else calculate the overlap of the x and y and multiply to get the result
    else:
        width = min((a[0] + a[2]),(b[0] + b[2])) - max(a[0],b[0])
        height = min((a[1] + a[2]),(b[1] + b[2])) - max(a[1],b[1])
        result = width*height
    return result

totalScore = 0

S1 = [1,5,3]
S2 = [5,6,2]
S3 = [2,1,2]
S4 = [9,6,2]
S5 = [7,2,3]
S6 = [3,2,5]
S7 = [5,3,1]

#---------- ---------- ---------- ---------- ----------
print( "Test 1: " + str(S1) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S1,S6)
r2 = overlap(S6,S1)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 2: " + str(S2) + str(S6) )
print( "Correct Answer: 2" )
r1 = overlap(S2,S6)
r2 = overlap(S6,S2)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 2:
    s1 = s1 + 1
if r2 == 2:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 3: " + str(S3) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S3,S6)
r2 = overlap(S6,S3)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 4: " + str(S4) + str(S6) )
print( "Correct Answer: 0" )
r1 = overlap(S4,S6)
r2 = overlap(S6,S4)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 0:
    s1 = s1 + 1
if r2 == 0:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 5: " + str(S5) + str(S6) )
print( "Correct Answer: 3" )
r1 = overlap(S5,S6)
r2 = overlap(S6,S5)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 3:
    s1 = s1 + 1
if r2 == 3:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 6: " + str(S6) + str(S6) )
print( "Correct Answer: 25" )
r1 = overlap(S6,S6)
r2 = overlap(S6,S6)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 25:
    s1 = s1 + 1
if r2 == 25:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print( "Test 7: " + str(S7) + str(S6) )
print( "Correct Answer: 1" )
r1 = overlap(S7,S6)
r2 = overlap(S6,S7)
print( "Result 1: " + str(r1) )
print( "Result 2: " + str(r2) )
s1 = 0
if r1 == 1:
    s1 = s1 + 1
if r2 == 1:
    s1 = s1 + 1
print( "Score: " + str(s1) )
print()

totalScore = totalScore + s1

#---------- ---------- ---------- ---------- ----------
print ( "Total Score: " + str(totalScore) )
print ( "Percentage: " + str(100*totalScore/14) )

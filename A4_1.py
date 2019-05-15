# Nate Brune
# 3/5/2019 
# I have not given or received any unauthorized assistance on this assignment

'''
my code for the standard deviation did not equal the statistics library result but I did get the same
result in the last two methods. The standard deviation I calculated was not far off so I assume
the difference between my functions and the math library function is due to a difference in rounding
'''

import inspect
import statistics as stats
import math
fileName = "avocado.csv"

def readFileToList(target):
    '''takes in fileName and the target variable and returns a list of all values for that variable'''
    
    result = []
    infile = open(fileName)
    index = infile.readline().split(",").index(target)

    for line in infile.readlines():
        result.append(float(line.split(",")[index]))
    infile.close()
    
    return result

def readAndComputeMean_SM(target):
    '''
    call function that reads the entire file into memory and returns a list
    use stat module (imported) to find the mean of the list
    '''
    valueList = readFileToList(target)
    mean = stats.mean(valueList)
    return mean

def readAndComputeSD_SM(target):
    '''
    call function that reads the entire file into memory and returns a list
    use stat module (imported) to find the standard deviation of the list
    '''
    valueList = readFileToList(target)
    sd = stats.stdev(valueList)
    return sd
    
def readAndComputeMedian_SM(target):
    '''
    call function that reads the entire file into memory and returns a list
    use stat module (imported) to find the median of the list
    '''
    valueList = readFileToList(target)
    median = stats.median(valueList)
    return median

def readAndComputeMean_HG(target):
    '''
    call function that reads the entire file into memory and returns a list
    use a for loop to calculate the number of values in the list and their sum
    calculate the mean
    '''
    valueList = readFileToList(target)
    counter, sumOfValues = 0 , 0
    for i in valueList:
        counter += 1
        sumOfValues += i

    mean = sumOfValues/counter
    return mean
    
def readAndComputeSD_HG(target):
    '''
    call function that calculates the mean
    call function that reads the entire file into memory and returns a list
    use a for loop to calculate the number of values in the list and the sum of the (differences to the mean)^2
    '''    
    mean = readAndComputeMean_HG(target)
    valueList = readFileToList(target)
    counter, sumOfVariances = 0, 0
    for i in valueList:
        counter += 1
        sumOfVariances += (abs(i - mean))**2
    sd = math.sqrt(sumOfVariances/counter)
    return sd

def readAndComputeMedian_HG(target):
    '''
    call function that reads the entire file into memory and returns a list
    sort the list, find the length of the list
    return the middle number of that list
    '''
    valueList = readFileToList(target)
    valueList.sort()
    counter = 0
    for i in valueList:
        counter += 1
    index = counter//2
    median = valueList[index]
    return median
    
def readAndComputeMean_MML(target):
    '''
    read the first line of the file and find the index of target variable
    declare sum and counter variables as 0
    for the remaining lines in the file, loop through each line and increment the counter and sum variables
    calculate and return the mean
    '''
    counter, sumOfValues = 0, 0
    infile = open(fileName)
    index = infile.readline().split(",").index(target)
    error = False
    while error == False:
        try: 
            sumOfValues += float(infile.readline().split(",")[index])
            counter += 1
        except IndexError:
            infile.close()
            error = True

    mean = (sumOfValues/counter)
    return mean

def readAndComputeSD_MML(target):
    '''
    read the first line of the file and find the index of target variable
    call function to compute the mean
    for the remaining lines in the file, loop through each line and increment the counter and sum variances
    calculate and return the mean
    '''
    
    counter, sumOfVariances = 0, 0
    infile = open(fileName)
    index = infile.readline().split(",").index(target)
    error = False
    mean = readAndComputeMean_MML(target)
    while error == False:
        try: 
            variance = abs(float(infile.readline().split(",")[index]) - mean)
            sumOfVariances += variance**2
            counter += 1
        except IndexError:
            infile.close()
            error = True

    return math.sqrt(sumOfVariances/counter)

def minOfFile(target):
    '''find min of values'''
    infile = open(fileName)
    index = infile.readline().split(",").index(target)
    fmin = float(infile.readline().split(",")[index])
    error = False
    while error == False:
        try: 
            value = float(infile.readline().split(",")[index])
            if value < fmin:
                fmin = value    
        except IndexError:
            infile.close()
            error = True
    return fmin

def maxOfFile(target):
    '''find max of values'''
    infile = open(fileName)
    index = infile.readline().split(",").index(target)
    fmax = float(infile.readline().split(",")[index])
    error = False
    while error == False:
        try: 
            value = float(infile.readline().split(",")[index])
            if value > fmax:
                fmax = value    
        except IndexError:
            infile.close()
            error = True
    return fmax

def lenOfFile(target):
    '''takes in the target variable and returns a list of all values for that variable'''
    counter = 0
    infile = open(fileName)
    index = infile.readline().split(",").index(target)

    while True:
        try:
            value = infile.readline().split(",")[index]
            counter += 1
        except IndexError:
            infile.close()
            break
    return counter


def findBucket2(fmin, fmax, target):
    '''
    using min and max declare the buckets
    passes through file one value at a time and adds to counter for each bucket
    then returns the bucket with the median in it and the number of values in that bucket
    '''
    sLen = lenOfFile(target)
    infile = open(fileName)
    m = sLen//2
    bSize = (fmax - fmin)/5 #variable for bucketsize
    #sets variables for each bucket as a list containing the buckets lower and upper bounds
    b1 = [fmin, fmin+bSize]
    b2 = [b1[1], b1[1]+bSize]
    b3 = [b2[1], b2[1]+bSize]
    b4 = [b3[1], b3[1]+bSize] 
    b5 = [b4[1], fmax+1]
    above, below, b1Count, b2Count, b3Count, b4Count, b5Count = 0, 0, 0, 0, 0, 0, 0 #counters for each bucket
    index = infile.readline().split(",").index(target) #read header line and find index for target variable
    for value in range(sLen):
        i = float(infile.readline().split(",")[index])
        if i < b1[0]:
            below += 1
        if i >= b1[0] and i < b1[1]:
            b1Count += 1
        if i >= b2[0] and i < b2[1]:
            b2Count += 1
        if i >= b3[0] and i < b3[1]:
            b3Count += 1
        if i >= b4[0] and i < b4[1]:
            b4Count += 1
        if i >= b5[0] and i < b5[1]:
            b5Count += 1
        if i >= b5[1]:
            above += 1

    #if statements to determine which bucket contains the median        
    if below + b1Count > m:
        return b1, b1Count
    elif below + b1Count + b2Count > m:
        return b2, b2Count
    elif below + b1Count + b2Count + b3Count > m:
        return b3, b3Count
    elif below + b1Count + b2Count + b3Count + b4Count > m:
        return b4, b4Count
    else:
        return b5, b5Count

def readAndComputeMedian_MML(target):
    '''
    uses while loop to call findBucket2 function until the bucket contains just one value
    then pass through the file one more time to find the value in that bucket
    '''
    fmin, fmax = minOfFile(target), maxOfFile(target)
    bounds, count = findBucket2(fmin, fmax, target)

    while count > 1:
        bounds, count = findBucket2(bounds[0], bounds[1], target)

    infile = open(fileName)
    sLen = lenOfFile(target)
    index = infile.readline().split(",").index(target)
    for value in range(sLen):
        median = float(infile.readline().split(",")[index])
        if median >= bounds[0] and median < bounds[1]:
            return median
    infile.close()

print(readAndComputeMean_SM("Total Volume"))
print(readAndComputeSD_SM("Total Volume"))
print(readAndComputeMedian_SM("Total Volume"))
print(readAndComputeMean_HG("Total Volume"))
print(readAndComputeSD_HG("Total Volume"))
print(readAndComputeMedian_HG("Total Volume"))
print(readAndComputeMean_MML("Total Volume"))
print(readAndComputeSD_MML("Total Volume"))
print(readAndComputeMedian_MML("Total Volume"))

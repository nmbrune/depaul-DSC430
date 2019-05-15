# Nate Brune
# 1/22/2019 
# I have not given or received any unauthorized assistance on this assignment

def prime(x):
    '''determines if an integer is prime
    returns a value of true if the number is prime and a value of false if it is not prime
    the function expects a positive, non-zero integer'''
    
    res = True #sets the result to True as a default
    for n in range(2,(x//2 + 1)): #loops to see if x is divisible by any numbers in the range of 2 to x//2
        if x % n == 0:
            res = False
            break
    return res


def digitSquareAndAdd(x):
    '''squares each digit of an integer and returns the sum of those squares'''
    res = 0
    for n in range(0,len(str(x))):
        res += int((str(x)[n]))**2
    return res

def happy(x):
    '''determines if an integer is happy
    returns True if an integer is happy and False if it is not happy
    expects an integer as input'''
    firstInt = x
    attemptLst = []
    loopAgain = True

    if digitSquareAndAdd(firstInt) == 1:
        res = True
    else:
        loopingInt = firstInt
        while loopAgain == True:
            attempt = digitSquareAndAdd(loopingInt)
            if attempt == 1:
                res = True
                loopAgain = False
            elif attempt in attemptLst:
                res = False
                loopAgain = False
            else:
                attemptLst.append(attempt)
                loopingInt = attempt
    return res


def happyPrime(x):
    '''determines if an integer is a happy prime number by calling the happy and prime functions
    expects an integer as input'''
    if happy(x) and prime(x) == True:
        return True
    else:
        return False


#printing first 20 prime numbers
print("printing first 20 prime numbers")
counterPrime = 0
loopingPrime = 2
while counterPrime < 20:
    if prime(loopingPrime) == True:
        print(loopingPrime)
        counterPrime += 1
    loopingPrime += 1


#printing first 20 happy numbers
print("printing first 20 happy numbers")
counterHappy = 0
loopingHappy = 2
while counterHappy < 20:
    if happy(loopingHappy) == True:
        print(loopingHappy)
        counterHappy += 1
    loopingHappy += 1


#printing first 20 happy prime numbers
print("printing first 20 happy prime numbers")
counterHappyPrime = 0
loopingHappyPrime = 2
while counterHappyPrime < 20:
    if happyPrime(loopingHappyPrime) == True:
        print(loopingHappyPrime)
        counterHappyPrime += 1
    loopingHappyPrime += 1


#printing first 20 sad prime numbers
print("printing first 20 sad prime numbers")
counterSadPrime = 0
loopingSadPrime = 2
while counterSadPrime < 20:
    if happyPrime(loopingSadPrime) == False:
        print(loopingSadPrime)
        counterSadPrime += 1
    loopingSadPrime += 1


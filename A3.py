# Nate Brune
# 2/19/2019 
# I have not given or received any unauthorized assistance on this assignment

import random

class SixSidedDie:
    
    def roll(self):
        'roll the dice, return a number 1-6'
        self.r = random.randint(1,6)
        return self.r
        
    def getFaceValue(self):
        'return face value from roll'
        return self.r
    
    def __repr__(self):
        'return formal representation'
        #return "{}({})".format(_name_,self.r)
        return "SixSidedDie({})".format(self.r)

class TenSidedDie(SixSidedDie):
    
    def roll(self):
        'roll the dice, return a number 1-10'
        self.r = random.randint(1,10)
        return self.r
    def __repr__(self):
        'return formal representation'
        return "TenSidedDie({})".format(self.r)
        
class TwentySidedDie(SixSidedDie):
    
    def roll(self):
        'roll the dice, return a number 1-20'
        self.r = random.randint(1,20)
        return self.r
    def __repr__(self):
        'return formal representation'
        return "TwentySidedDie({})".format(self.r)


class Cup:
    
    def __init__(self,six=1,ten=1,twenty=1):
        'defines the cup'
        self.six, self.ten, self.twenty = six, ten, twenty
        self.cup = []
        for i in range(0,self.six):
            d = SixSidedDie()
            self.cup.append(d)
        
        for i in range(0,self.ten):
            d = TenSidedDie()
            self.cup.append(d)
        
        for i in range(0,self.twenty):
            d = TwentySidedDie()
            self.cup.append(d)
    
    def roll(self):
        'rolls all dice in the cup and returns the sum'
        self.cupValues = []
        for d in self.cup:
            self.cupValues.append(d.roll())
        return sum(self.cupValues)
    
    def getSum(self):
        'returns the sum from the previous roll'
        return sum(self.cupValues)
    
    def __repr__(self):
        'returns contents of the cup'
        return "Cup{}".format(tuple(self.cup))
        

#example of a cup with specified values and the functionality
cup1 = Cup(2,3,4)
print(cup1.roll())
print("You rolled a total value of " + str(cup1.getSum()))
print(cup1)

#example of a cup without specified values and the functionality
cup2 = Cup()
print(cup2.roll())
print("You rolled a total value of " + str(cup2.getSum()))
print(cup2)


def askToPlay():
    '''Asks user if they would like to play again and returns a True or False value'''
    play = ''
    while play != 'y':
        play = str(input("Do you want to play?(y/n) "))
        if play == 'n':
            print("Goodbye")
            return False
        elif play == 'y':
            print("Let's play!")
            return True
        else:
            print("Invalid Entry: must enter either y or n")


def takeBet(balance):
    '''asks user to place bet and validates that bet is a positive integer greater than zero
    takes user's balance as input and returns the user's bet'''
    bet = 0
    while bet <= 0 or bet > balance:
        try:
            bet = int(input("Enter your bet (ex. 10): "))
        except:
            print("Invalid Entry: must enter whole number")
        if bet <= 0:
            print("Bet must be a positive number greater than zero")
        elif bet > balance:
            print("Bet cannot be greater than your balance of " + str(balance))     
    return bet


def nDice(str):
    '''asks user how many of the type of die (input) they would like to use
    makes sure entry is valid and then returns the number of die'''
    n = -1
    while n < 0:
        try:
            n = int(input("Enter number of " + str + " you want to play (ex. 1): "))
        except:
            print("Invalid Entry: must enter whole number")
        if n < 0:
            print("Enter a positive number")
    return n


def playGame(goal):
    '''asks user how many of each die they would like to play
    plays the game and returns the multiplier for the bet'''
    
    nSix = nDice('SixSidedDie')
    nTen = nDice('TenSidedDie')
    nTwenty = nDice('TwentySidedDie')
    
    cup = Cup(nSix,nTen,nTwenty)
    result = cup.roll()
    print("You rolled a total value of " + str(cup.getSum()))
    dif = goal - cup.getSum()
    
    if dif < 0:
        return -1
    elif dif == 0:
        return 10
    elif dif <= 5:
        return 5
    elif dif <= 10:
        return 2
    else:
        return -1


#kick off game by asking for user's name, default userName set to 'user1'
userName = str(input("Hello, please enter your userName (if nothing is entered, default will be 'user1'): "))
if userName == '':
    userName = 'user1'
balance = 100
#Welcome the user, present them with their balance and explain the rules
print('''Welcome ''' + userName + '''! Your starting balance is $100\n
\n
Here's how to play:\n
- You will be presented with a goal\n
- You're trying to roll a value as close to the goal as possible without going over\n
- You will get to choose how many six, ten, and twenty sided die you want to play with\n
\n
\t- If hit the goal you recieve 10x your bet\n
\t- If you're within 5 you recieve 5x your bet\n
\t- If you're within 10 you recieve 2x your bet\n
\t- Anything over the goal or outside of 10 from the goal and you will lose your bet''')


play = True
while balance > 0 or play == True:  
    play = askToPlay()
    if play == False:
        break
    goal = random.randint(1,100)
    print("Your goal is " + str(goal))
    bet = takeBet(balance)
    multiplier = playGame(goal)
    balance = balance + (bet*multiplier)
    print(userName +" balance is now $" + str(balance))
    if balance == 0:
        print("Game Over")
        break


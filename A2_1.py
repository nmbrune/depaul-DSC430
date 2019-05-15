# Nate Brune
# 1/29/2019
# I have not given or received any unauthorized assistance on this assignment. 

def txtToNameList(txtFile):
    '''
    takes in the text file as input
    returns the contents of the file in the form of a list of names 
    (each name is stripped of escape characters)
    '''
    infile = open(txtFile)
    rawList = infile.readlines()
    stripList = []
    for name in rawList:
        stripList.append(name.strip())
    infile.close()
    return stripList

def listToNameDict(nameList, letterList):
    '''
    takes in the nameList created by txtToNameList and a letterList as input
    first it creates a dictionary (nameDict) with every item in the letterList as keys with a value of 0 as a default
    then uses the nameList to populate that dictionary with values for how many names end in each letter
    returns the nameDict
    '''
    nameDict = {}
    for letter in letterList:
        nameDict[letter] = 0
    for name in nameList:
        if name[-1] in nameDict:
            nameDict[name[-1]] += 1
    return nameDict

boys = txtToNameList('namesBoys.txt')
girls = txtToNameList('namesGirls.txt')

#creating list containing the last letters for all names
#this list will be one of the inputs for the listToNameDict function
allNames = boys + girls
letters = []
for name in allNames:
    if name[-1] not in letters:
        letters.append(name[-1])
letters.sort() #alphabetizing the list

boyNameDict = listToNameDict(boys, letters)
girlNameDict = listToNameDict(girls, letters)

#printing the names in a clean format
print("{:6}  {:4}  {:5}".format("Letter", "Boys", "Girls"))
for letter in letters:
    print("{:6}  {:4}  {:5}".format(letter,boyNameDict[letter],girlNameDict[letter]))

'''
An interesting difference I found in the boys and girls names is that the boys names are
more spread out amongst the letters, whereas the girls names had less diversity in last
letters. Also the two most popular ending letters shared by both boys and girls were 
'e' and 'n'
'''
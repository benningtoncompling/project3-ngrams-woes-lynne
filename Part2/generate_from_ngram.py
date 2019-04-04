import random
import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

def turnDiction(nDict):
    diction = {}
    getLines = [item.split() for item in nDict.split("\n")]
    total = len(getLines)
    for i in range(1,total):
        temp = getLines[i]
        string = ""
        for j in range(3,len(temp)):
            word = temp[j]
            if word != "</s>":
                string += word + " "
            else:
                string += word
        diction[string] = float(temp[1])
    return diction

def isStartOfPhrase(str1, str2):
    length = len(str1.split())
    temp1 = ' '.join(str1.split()[:length])
    temp2 = ' '.join(str2.split()[:length])
    if temp2 == temp1:
        return True
    return False

def uniGramGenerator(uniDict):
    ansStr = "<s> "
    while "</s>" not in ansStr:
        cap = random.random()
        sum = 0
        for item in uniDict:
            sum += uniDict[item]
            if sum >= cap and item != "<s> ":
                ansStr += item
                break
    return ansStr

def biGramGenerator(biDict):
    ansStr = "<s> "
    tempStr = "<s> "
    while "</s>" not in ansStr: 
        cap = random.random()
        sum = 0
        for item in biDict:
            if isStartOfPhrase(tempStr,item):
                sum += biDict[item]
                if sum >= cap:
                    tempStr = ' '.join(item.split()[1:])
                    ansStr += tempStr + " "
                    break
    return ansStr

def triGramGenerator(triDict):
    ansStr = "<s> "
    tempStr = "<s> "
    #Find Initial tempStr
    cap = random.random()
    sum = 0
    while len(tempStr.split()) < 2:
        for item in biDict:
            if isStartOfPhrase(tempStr, item):
                sum += biDict[item]
                if sum >= cap:
                    tempStr = item
                    break
    while "</s>" not in ansStr:
        cap = random.random()
        sum = 0
        for item in biDict:
            if isStartOfPhrase(tempStr, item):
                sum += biDict[item]
                if sum >= cap:
                    tempStr = ' '.join(item.split()[1:])
                    ansStr += tempStr + " "
                    break
    return ansStr

splitted = open(inputFile,"r", encoding = "UTF-8").read().split("\n\n")
uniDict = turnDiction(splitted[1])
biDict = turnDiction(splitted[2])
triDict = turnDiction(splitted[3])
uniGen = "\\1grams:\n"
biGen = "\\2grams:\n"
triGen = "\\3grams:\n"

for i in range(5):
    uniGen += uniGramGenerator(uniDict) + "\n"
    biGen += biGramGenerator(biDict) + "\n"
    triGen += triGramGenerator(triDict) + "\n"
outStr = uniGen + "\n" + biGen + "\n" + triGen
with open(outputFile, "w", encoding="UTF-8") as result:
    result.write(outStr)

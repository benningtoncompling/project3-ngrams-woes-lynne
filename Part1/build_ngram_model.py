import sys 
import math 

inputFile = sys.argv[1]
outputFile = sys.argv[2]
countU = 0

processed = ["<s> " + line.strip().lower() + " </s>" for line in open(
    inputFile, "r", encoding="UTF-8").readlines()]

#Returns a dictionary ordered based on value and alphabetical order
def orderDict(dictionary):
    dictionary = dict(sorted(dictionary.items()))
    dictionary = dict(
        sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    return dictionary

#Gives the ngram total count
def nGramTotal(ansDict):
    count = 0
    for key, value in ansDict.items():
        count += value[0]
    return count

#Gives the ngram count in a form of a string
def nGramOut(ansDict, n):
    ans = "\\" + str(n) + "-grams:\n"
    diction = orderDict(ansDict)
    count = 0
    for key, value in diction.items():
        print(count)
        count += 1
        ans += str(value[0]) + " " + str(value[0]/value[1]) + " " + \
            str(math.log10(value[0]/value[1])) + " " + key + "\n"
    return ans

#Gives the unigram total count
def uniGramTotal(ansDict):
    count = 0
    for key, value in ansDict.items():
        count += value
    return count

#Finds and counts all existing Unigrams and returns a dictionary
def uniGramCount(processed):
    ansDict = {}
    for item in processed:
        temp = item.split()
        for token in temp:
            if token in ansDict:
                ansDict[token] += 1
            else:
                ansDict[token] = 1
    return ansDict 

#Gives the unigram count in a form of a string
def uniGramOut(ansDict, count):
    ans = "\\1-grams:\n"
    diction = orderDict(ansDict)
    count1 = 0 
    for key,value in diction.items():
        print(count1)
        count1 += 1
        ans += str(value) + " " + str(value/count) + " " + str(math.log10(value/count)) + " " + key + "\n"
    return ans 

#Finds and counts all existing Bigrams and returns a dictionary
def biGramCount(processed, ansU):
    ansDict = {}
    for item in processed:
        tempItem = item.split()
        temp = len(tempItem)
        for i in range(temp):
            if i+1<temp:
                string = tempItem[i] + " " + tempItem[i+1]
                if string in ansDict:
                    ansDict[string][0] += 1
                else:
                    ansDict[string] = []
                    ansDict[string].append(1)
                    ansDict[string].append(ansU[tempItem[i]])
            else:
                continue
    return ansDict

#Finds and counts all existing Trigrams and returns a dictionary
def triGramCount(processed, ansB):
    ansDict = {}
    for item in processed:
        tempItem = item.split()
        temp = len(tempItem)
        for i in range(temp):
            if i+2 < temp:
                string1 = tempItem[i] + " " + tempItem[i+1] + " " + tempItem[i+2]
                string2 = tempItem[i] + " " + tempItem[i+1]
                if string1 in ansDict:
                    ansDict[string1][0] += 1
                else:
                    ansDict[string1] = []
                    ansDict[string1].append(1)
                    ansDict[string1].append(ansB[string2][0])
            else:
                continue
    return ansDict

ansU = uniGramCount(processed)
countU = uniGramTotal(ansU)
ansB = biGramCount(processed,ansU)
countB = nGramTotal(ansB)
ansT = triGramCount(processed,ansB)
countT = nGramTotal(ansT)

#This is the output part
ansStr = ""
data = "\\data\\\n"
data += "ngram 1: type=" + str(len(ansU)) + " token=" + str(countU) + "\n"
data += "ngram 2: type=" + str(len(ansB)) + " token=" + str(countB) + "\n"
data += "ngram 3: type=" + str(len(ansT)) + " token=" + str(countT) + "\n"

uOut = uniGramOut(ansU, countU)
bOut = nGramOut(ansB, 2)
tOut = nGramOut(ansT, 3)

ansStr += data + "\n"
ansStr += uOut + "\n"
ansStr += bOut + "\n"
ansStr += tOut + "\n" + "\\end\\"

with open(outputFile, "w", encoding="UTF-8") as result:
    result.write(ansStr)

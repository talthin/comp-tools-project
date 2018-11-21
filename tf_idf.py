from sklearn.feature_extraction.text import TfidfVectorizer
import mapping
import math
import re
from collections import Counter


d = {}
d2 = {}

def computeTF(wordDict):
    tfdict = {}
    dictCount = len(wordDict)
    for word, count in wordDict.items():
        tfdict[word] = count / float(dictCount)
    return (tfdict)


# TODO, ONLY COUNT OCCURENCE ONCE PER DOCUMENT
def computeIDF(docList):
    idfDict = {}
    N = len(docList)


    for i in range(len(docList)):
        for word in docList[i]:
            if word in idfDict:
                idfDict[word] += 1
            else:
                idfDict[word] = 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/float(val))
        # print(idfDict[word])
    return idfDict

def computeTF_IDF(doclist, IDFdict):

    tfidf= {}
    unionSet = dict(Counter(doclist[0]) + Counter(doclist[1]))

    for word, val in unionSet.items():
        tfidf[word] = val * IDFdict[word]

    return tfidf


with open("phymap.txt") as f:
    for line in f:
        # print(line)
        (key, val) = line.split()
        d[key] = int(val)

with open("culmap.txt") as f:
    for line in f:
        # print(line)
        (key, val) = line.split()
        d2[key] = int(val)

# dList = list(d.keys())
# d2List = list(d2.keys())
# wordset = set(dlist).union(set(d2list))



computeTF(d)
idfs = computeIDF([d, d2])
tfidf = computeTF_IDF([d, d2], idfs)
print(tfidf)


# print(idfs)

# print(d)
# data1 = F1.read()
# data2 = F2.read()
# Fit the TfIdf model

# # Transform a document into TfIdf coordinates
# X = TfidfVectorizer.transform(data1)

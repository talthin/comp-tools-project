from sklearn.feature_extraction.text import TfidfVectorizer
import mapping
import math
import re
import sys
from collections import Counter


doclist = []
for arg in sys.argv[1:]:
    wordDict = {}
    with open(arg) as f:
        for line in f:
            # print(line)
            (key, val) = line.split()
            wordDict[key] = int(val)
    doclist.append(wordDict)

# d = {}
# d2 = {}

# def computeTF(wordDict):
#     tfdict = {}
#     dictCount = len(wordDict)
#     for word, count in wordDict.items():
#         tfdict[word] = count / float(dictCount)
#     return (tfdict)


def computeIDF(doclist):
    idfDict = {}
    N = len(doclist)


    for i in range(len(doclist)):
        for word in doclist[i]:
            if word in idfDict:
                idfDict[word] += 1
            else:
                idfDict[word] = 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/float(val))
        # print(idfDict[word])
    return idfDict

def computeTF_IDF(doclist, IDFdict):

    tfidf_dicts = []
    for i in range(len(doclist)):
        tfidf_dicts.append(doclist[i])

    for wdict in tfidf_dicts:
        for word, val in wdict.items():
            wdict[word] = val * IDFdict[word]

    # tfidf = {}
    # unionSet = dict(Counter(doclist[0]) + Counter(doclist[1]))
    # for word, val in unionSet.items():
    #     tfidf[word] = val * IDFdict[word]

    return tfidf_dicts



idfs = computeIDF(doclist)
tfidf = computeTF_IDF(doclist, idfs)
print(tfidf)
# print(tfidf[1])

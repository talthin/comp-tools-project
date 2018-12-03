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
            (key, val) = line.split()
            wordDict[key] = int(val)
    doclist.append(wordDict)

# dont need tf because we already count word frequency
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


def topWordsTf_IDF(tf_idf,amount):
    sortedTf_IDF = sorted(tf_idf, key=tf_idf.get, reverse=True)
    topWords = sortedTf_IDF[:amount]
    return topWords

idfs = computeIDF(doclist)
tfidf = computeTF_IDF(doclist, idfs)
topwords = topWordsTf_IDF(tfidf[6], 20)

print(topwords)
# print(tfidf[1])

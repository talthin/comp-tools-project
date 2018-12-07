from sklearn.feature_extraction.text import TfidfVectorizer
import mapping
import math
import re
import sys
from collections import Counter



def tf_idf_init():
    listofD = [
        "countData/Culture.txt",
        "countData/Formal sciences.txt",
        "countData/Geography.txt",
        "countData/Historiography.txt",
        "countData/Personal life.txt",
        "countData/Physics.txt",
        "countData/Religion.txt",
        "countData/Social Sciences.txt",
    ]

    doclist = []
    for arg in listofD:
        wordDict = {}
        with open(arg) as f:
            for line in f:
                # print(line)
                (key, val) = line.split()
                key = key.replace('"','')
                wordDict[key] = int(val)
        doclist.append(wordDict)
        for word in wordDict:
            wordDict[word] = float(wordDict[word])/len(wordDict)
    return doclist

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

    return tfidf_dicts


def ToptfidfWeights(tfidf,N):
    TopTF = []
    for i in range(len(tfidf)):
        res=dict(sorted([(k,v) for k, v in tfidf[i].items()], key=lambda x: x[1])[-N:])
        TopTF.append(res)
    return TopTF


def calculate_hitrate(label_list, result_list):

    hit = 0
    culhit = 0
    culcount = 0
    for_sci_hit = 0
    for_sci_count = 0
    geo_count = 0
    geo_hit = 0
    his_count = 0
    his_hit = 0
    per_life_count = 0
    per_life_hit = 0
    phy_count = 0
    phy_hit = 0
    rel_count = 0
    rel_hit = 0
    soc_sci_count = 0
    soc_sci_hit = 0

    for j in range(len(label_list)):
        if label_list[j] == "Culture":
            culcount += 1
            if result_list[j] == 0:
                culhit += 1
        if label_list[j] == "Formal sciences":
            for_sci_count += 1
            if result_list[j] == 1:
                for_sci_hit += 1
        if label_list[j] == "Geography":
            geo_count += 1
            if result_list[j] == 2:
                geo_hit += 1
        if label_list[j] == "Historiography":
            his_count += 1
            if result_list[j] == 3:
                his_hit += 1
        if label_list[j] == "Personal life":
            per_life_count += 1
            if result_list[j] == 4:
                per_life_hit += 1
        if label_list[j] == "Physics":
            phy_count += 1
            if result_list[j] == 5:
                phy_hit += 1
        if label_list[j] == "Religion":
            rel_count += 1
            if result_list[j] == 6:
                rel_hit += 1
        if label_list[j] == "Social Sciences":
            soc_sci_count += 1
            if result_list[j] == 7:
                soc_sci_hit += 1
    hit = culhit + for_sci_hit + geo_hit + his_hit + per_life_hit + phy_hit + rel_hit + soc_sci_hit
    hit_precentage = float(hit / len(label_list))
    return hit_precentage

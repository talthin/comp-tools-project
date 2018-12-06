# import queryWiki
import os
import subprocess
import tf_idf_nocomm
import K_means_clustering
import wikipedia
import filter
import queryWiki
import clusterstuff
import DBSCAN

categoryList = [
    "Culture", "Formal sciences", "Geography", "Historiography",
    "Personal life", "Physics", "Religion", "Social Sciences"
]

testDataArticleList = queryWiki.createWikidict(categoryList)


# for cat in categoryList:

#     myinput = open('wikidata/' + cat + '.txt')
#     myoutput = open('countData/' + cat + '.txt', 'w')
#     p = subprocess.call(['python3','mapping.py'], stdin=myinput, stdout=myoutput)
#     myoutput.flush()


doclist = tf_idf_nocomm.tf_idf_init()
idf_dicts = tf_idf_nocomm.computeIDF(doclist)
tfidf_dicts = tf_idf_nocomm.computeTF_IDF(doclist,idf_dicts)

testArticles = []
labellist = []
for i in range(len(testDataArticleList)):
    labellist.append(testDataArticleList[i]["label"])
    testArticles.append(testDataArticleList[i]["txt"])
    


#topwords = 104
topword_i = []
tfidfacc = []
KMacc = []
DBacc = []
for topwords in range(8,200):
    topword_matrix = tf_idf_nocomm.ToptfidfWeights(tfidf_dicts, topwords)
    binary_topword_matrix  = K_means_clustering.generateBinaryWordMatrix(topword_matrix,topwords)

# print(topword_matrix[0])
## filter testarticles
# testArticles = []

    binary_articles = K_means_clustering.WordVec1Hot(topword_matrix,testArticles,topwords)

#print(binary_articles[100].count(1))

#result = clusterstuff.tf_idf_classifier(tfidf_dicts, idf_dicts, testArticles)
    resultDB = DBSCAN.DBSCAN(binary_articles,binary_topword_matrix,200,10)
    resultKM = K_means_clustering.K_means(binary_articles,binary_topword_matrix)
#print(resultDB)
#print(labellist)
#print(result)

# TODO CALCULATE HOW GOOOD YOU GUESS CATEGORIES

#hit_precentage = tf_idf_nocomm.calculate_hitrate(labellist, result)
    hit_precentageKM = tf_idf_nocomm.calculate_hitrate(labellist,resultKM)
    hit_precentageDB = tf_idf_nocomm.calculate_hitrate(labellist,resultDB)
    tfidfacc.append(hit_precentage)
    KMacc.append(hit_precentageKM)
    DBacc.append(hit_precentageDB)
    topword_i.append(topwords)
    print(topwords)
print("TF-IDF Score accuracy: " + str(hit_precentage))
print("K-means accuracy: " + str(hit_precentageKM))
print("DBSCAN accuracy: " + str(hit_precentageDB))

score = 0
finalTW = 0
for i in range(0,len(topword_i)):
    tempscore = 0
    tempscore = tfidfacc[i]+KMacc[i]+DBacc[i]
    if score == 0:
        score = tempscore
        finalTW = i
    elif tempscore > score:
        score = tempscore
        finalTW = i

import matplotlib.pyplot as plt

plt.plot(KMacc)
plt.plot(DBacc)
plt.ylabel("Accuracy")
plt.xlabel("Amount of top words")
plt.show()
        
print(score)
print(finalTW)
print(finalTW+8)

# binary_word_matrix = K_means_clustering.generateBinaryWordMatrix(
#     topword_matrix, topwords)

# article_matrix = K_means_clustering.WordVec1Hot(topword_matrix, testArticles,
#                                                 topwords)
# result = K_means_clustering.K_means(article_matrix, binary_word_matrix)

# for i in range(len(result)):
#     print(result[i][1][0])

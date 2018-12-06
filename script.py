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
import matplotlib.pyplot as plt
import time

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
    

topword_i = []
tfidfacc = []
KMacc = []
DBacc = []
time_K = []
time_DB = []
for topwords in range(8,200):
    start_time = time.clock()
    topword_matrix = tf_idf_nocomm.ToptfidfWeights(tfidf_dicts, topwords)
    binary_topword_matrix  = K_means_clustering.generateBinaryWordMatrix(topword_matrix,topwords)


    binary_articles = K_means_clustering.WordVec1Hot(topword_matrix,testArticles,topwords)
    init_time = time.clock()-start_time

    start_time_DB = time.clock()
    resultDB = DBSCAN.DBSCAN(binary_articles,binary_topword_matrix,1/len(binary_topword_matrix),len(binary_articles)/len(binary_topword_matrix))
    DB_time = time.clock()+init_time-start_time_DB
    
    start_time_K = time.clock()
    resultKM = K_means_clustering.K_means(binary_articles,binary_topword_matrix)
    K_time = time.clock()+init_time-start_time_K
    
    time_K.append(K_time)
    time_DB.append(DB_time)

    hit_precentageKM = tf_idf_nocomm.calculate_hitrate(labellist,resultKM)
    hit_precentageDB = tf_idf_nocomm.calculate_hitrate(labellist,resultDB)
    KMacc.append(hit_precentageKM)
    DBacc.append(hit_precentageDB)
    topword_i.append(topwords)
    print(topwords)

plt.plot(KMacc)
plt.plot(DBacc)
plt.ylabel("Accuracy")
plt.xlabel("Amount of top words")
plt.show()

plt.plot(time_K)
plt.plot(time_DB)
plt.ylabel("Computational time")
plt.xlabel("Amount of top words")
plt.show()

tf_start = time.clock()
result = clusterstuff.tf_idf_classifier(tfidf_dicts, idf_dicts, testArticles)
hit_percentage = tf_idf_nocomm.calculate_hitrate(labellist, result)
tf_time = time.clock()-tf_start

print("TF-IDF Score accuracy: " + str(hit_percentage))
print("K-means accuracy: " + str(max(KMacc)))
print("DBSCAN accuracy: " + str(max(DBacc)))
print("Number of topwords for K-Means: " + str(KMacc.index(max(KMacc))+8))
print("Number of topwords for DBSCAN: " + str(DBacc.index(max(DBacc))+8))

print("Computational time for K-Means: " + str(tf_time))
print("Computational time for K-Means: " + str(time_K[KMacc.index(max(KMacc))]))
print("Computational time for DBSCAN: " + str(time_DB[DBacc.index(max(DBacc))]))

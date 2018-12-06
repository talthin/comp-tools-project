# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:21:39 2018

@author: Frederik
"""

import matplotlib.pyplot as plt

plt.plot(topword_i, KMacc, color='b')
plt.plot(topword_i, DBacc, color='r')
plt.ylabel("Accuracy")
plt.xlabel("Amount of top words")
plt.show()

plt.plot(topword_i, time_K, color='b')
plt.plot(topword_i, time_DB, color='r')
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
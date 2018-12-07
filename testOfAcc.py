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
result = tf_idf_classifier.tf_idf_classifier(tfidf_dicts, idf_dicts,
                                             testArticles)
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

best_KM = result_KM[KMacc.index(max(KMacc))]
best_DB = result_DB[DBacc.index(max(DBacc))]
table_result = []
for j in range(0,len(labellist)):
    if best_KM[j] == 0:
        best_KM[j] = "Culture"
    if best_KM[j] == 1:
        best_KM[j] = "Formal sciences"
    if best_KM[j] == 2:
        best_KM[j] = "Geography"
    if best_KM[j] == 3:
        best_KM[j] = "Historiography"
    if best_KM[j] == 4:
        best_KM[j] = "Personal life"
    if best_KM[j] == 5:
        best_KM[j] = "Physics"
    if best_KM[j] == 6:
        best_KM[j] = "Religion"
    if best_KM[j] == 7:
        best_KM[j] = "Social Sciences"
    if best_DB[j] == "None":
        continue
    if best_DB[j] == 0:
        best_DB[j] = "Culture"
    if best_DB[j] == 1:
        best_DB[j] = "Formal sciences"
    if best_DB[j] == 2:
        best_DB[j] = "Geography"
    if best_DB[j] == 3:
        best_DB[j] = "Historiography"
    if best_DB[j] == 4:
        best_DB[j] = "Personal life"
    if best_DB[j] == 5:
        best_DB[j] = "Physics"
    if best_DB[j] == 6:
        best_DB[j] = "Religion"
    if best_DB[j] == 7:
        best_DB[j] = "Social Sciences"
    if result[j] == 0:
        result[j] = "Culture"
    if result[j] == 1:
        result[j] = "Formal sciences"
    if result[j] == 2:
        result[j] = "Geography"
    if result[j] == 3:
        result[j] = "Historiography"
    if result[j] == 4:
        result[j] = "Personal life"
    if result[j] == 5:
        result[j] = "Physics"
    if result[j] == 6:
        result[j] = "Religion"
    if result[j] == 7:
        result[j] = "Social Sciences"
    print(str(j+1) + "&" + str(labellist[j]) + "&" + str(result[j]) + "&" + str(best_KM[j]) + "&" + str(best_DB[j]) + " \\\\" + " \hline")
    
    
# import queryWiki
import os
import subprocess
import tf_idf_nocomm
import K_means_clustering
import wikipedia
import filter
import queryWiki
import clusterstuff

topwords = 50
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
topword_matrix = tf_idf_nocomm.ToptfidfWeights(tfidf_dicts, topwords)

# print(topword_matrix[0])
## filter testarticles
# testArticles = []

testArticles = []
labellist = []
for i in range(len(testDataArticleList)):
    labellist.append(testDataArticleList[i]["label"])
    testArticles.append(testDataArticleList[i]["txt"])

result = clusterstuff.tf_idf_classifier(tfidf_dicts, idf_dicts, testArticles)
print(labellist)
print(result)

# TODO CALCULATE HOW GOOOD YOU GUESS CATEGORIES

hit_precentage = tf_idf_nocomm.calculate_hitrate(labellist, result)
print(hit_precentage)

# binary_word_matrix = K_means_clustering.generateBinaryWordMatrix(
#     topword_matrix, topwords)

# article_matrix = K_means_clustering.WordVec1Hot(topword_matrix, testArticles,
#                                                 topwords)
# result = K_means_clustering.K_means(article_matrix, binary_word_matrix)

# for i in range(len(result)):
#     print(result[i][1][0])

# import queryWiki
import os
import subprocess
import tf_idf_nocomm

topwords = 100
categoryList = [
    "Culture", "Formal sciences", "Geography", "Historiography",
    "Personal life", "Physics", "Religion", "Social Sciences"
]

for cat in categoryList:

    myinput = open('wikidata/' + cat + '.txt')
    myoutput = open('countData/' + cat + '.txt', 'w')
    p = subprocess.call(['python3','mapping.py'], stdin=myinput, stdout=myoutput)
    myoutput.flush()


doclist = tf_idf_nocomm.tf_idf_init()
idf_dicts = tf_idf_nocomm.computeIDF(doclist)
tfidf_dicts = tf_idf_nocomm.computeTF_IDF(doclist,idf_dicts)
topword_matrix = tf_idf_nocomm.ToptfidfWeights(tfidf_dicts, topwords)

print(topword_matrix[0])


import tf_idf_nocomm
import filter
import wikipedia



No = 100
doclist = tf_idf_nocomm.tf_idf_init()
idf = tf_idf_nocomm.computeIDF(doclist)
tfidf = tf_idf_nocomm.computeTF_IDF(doclist,idf)
TopTF = tf_idf_nocomm.ToptfidfWeights(tfidf,N)

testVec = []

for i in range(len(TopTF)):
    temp = [0]*No*len(TopTF)
    for j in range(len(TopTF[i])):
        temp[j+i*No] = 1
    testVec.append(temp)
    
#print(testVec[0].count(1))

#print(idf)
    
dk = wikipedia.page("Denmark")
dk = dk.content
article = filter.remove_all_but_words(dk)
article = filter.remove_stopwords(article)

#print(len(tfidf[5]))

#print(TopTF[5]["varphi"])

def gay_classifier(tfidf,idf,TopTF,testVec, article,No):
    n = len(tfidf) #Amount of clusters (aka amount of categories in MoD)
    m = No*len(TopTF) #Amount of words in our vocabulary
    ArtVec = [0]*n*m
    
    for i in range(len(TopTF)):
        for j in range(len(TopTF[i])):
            if list(TopTF[i].keys())[j] in article:
                ArtVec[j+i*No] = 1
                
        
    return ArtVec




print(gay_classifier(tfidf,idf,TopTF,testVec,article,No))
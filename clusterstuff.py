
import tf_idf
import filter
import wikipedia

doclist = tf_idf.tf_idf_init()
idf = tf_idf.computeIDF(doclist)
tfidf = tf_idf.computeTF_IDF(doclist,idf)

#print(idf)

dk = wikipedia.page("Denmark")
dk = dk.content
article = filter.remove_all_but_words(dk)
article = filter.remove_stopwords(article)

#print(len(tfidf[5]))


def tf_idf_classifier(tfidf,idf,article):
    N = len(tfidf) #Amount of clusters (aka amount of categories in MoD)
    m = len(idf) #Amount of words in our vocabulary
    
    label = []
    
    dictart = {}
    
    for word in article:
        if word in idf:
            if word in dictart:
                dictart[word] += 1
            else:
                dictart[word] = 1
        
    L = None
    LNN = 0
    for i in range(0,N):
        nn = 0
        for word in dictart:
            #nn += (tfidf[i][word]-dictart[word]*tfidf[i][word])**2
            if word not in tfidf[i]:
                continue
            else:
                nn += tfidf[i][word]*dictart[word]
            
        #nn = nn**(0.5)
        print(nn)
        if L == None:
            L = i
            LNN = nn
        elif nn > LNN:
            L = i
            LNN = nn
            
    label.append(L)
    return label

print(tf_idf_classifier(tfidf,idf,article))

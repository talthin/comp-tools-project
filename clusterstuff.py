import tf_idf_nocomm
import filter
import wikipedia

#doclist = tf_idf_nocomm.tf_idf_init()
#idf = tf_idf_nocomm.computeIDF(doclist)
#tfidf = tf_idf_nocomm.computeTF_IDF(doclist,idf)

#print(idf)

#article = []

#dk = wikipedia.page("Denmark")
#Swe = wikipedia.page("Christianity")
#dk = dk.content
#Swe = Swe.content
#dk = filter.remove_all_but_words(dk)
#dk = filter.remove_stopwords(dk)
#Swe = filter.remove_all_but_words(Swe)
#Swe = filter.remove_stopwords(Swe)

#article.append(dk)
#article.append(Swe)

#print(len(tfidf[5]))

#test = dk

def tf_idf_classifier(tfidf,idf,article):
    N = len(tfidf) #Amount of clusters (aka amount of categories in MoD)
    m = len(idf) #Amount of words in our vocabulary
    label = []
    
    for j in range(0,len(article)):
        dictart = {}
        for word in article[j]:
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
            #print(nn)
            if L == None:
                L = i
                LNN = nn
            elif nn > LNN:
                L = i
                LNN = nn
            
        label.append(L)
    return label

#print(tf_idf_classifier(tfidf,idf,article))

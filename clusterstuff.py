import tf_idf_nocomm
import filter
import wikipedia

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
                if word not in tfidf[i]:
                    continue
                else:
                    nn += tfidf[i][word]*dictart[word]
            
            if L == None:
                L = i
                LNN = nn
            elif nn > LNN:
                L = i
                LNN = nn
            
        label.append(L)
    return label

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

def WordVec1Hot(tfidf,idf,TopTF,testVec, article,No):
    n = len(tfidf) #Amount of clusters (aka amount of categories in MoD)
    m = No*len(TopTF) #Amount of words in our vocabulary
    ArtVec = [0]*m
    
    for i in range(len(TopTF)):
        for j in range(len(TopTF[i])):
            if list(TopTF[i].keys())[j] in article:
                ArtVec[j+i*No] = 1
                
        
    return ArtVec


def computeDist (point, center):
    EucDist = 0
    for j in range(len(point)):
        EucDist += (point[j]-center[j])**2
        
    EucDist = EucDist**(0.5)
    
    return EucDist

def defineTFcenter(TopTF):
    center = []
    for i in range(len(TopTF)):
        center.append(TopTF[i])
    
    return center

def computeLabel (ArtVec,center,dist):
    idx_min = min(dist,key= dist.get)
    return [idx_min,ArtVec,center[idx_min]]

def updateCenter(cluster_lab,center):
    newCenter = [0]*len(center)
    
    for i in range(len(center)):
        w_centers = 50 #Weight is 50 as the centers are built on a lot of articles
        newCenter[i] = (center[i]+cluster_lab[i]/w_centers)/2
    
    return newCenter

def K_means(ArtVec,testVec):
    center = defineTFcenter(testVec)
    label = []
    cluster_lab =[]
    N = len(ArtVec)
    K = len(center)
    
    for i in range(0,100):
        #for j in range(0,N):
            dist = {}
            for c in range(0,K):
                dist[c] = computeDist(ArtVec,center[c])
            label = computeLabel(ArtVec,center,dist)
            center[label[0]] = updateCenter(label[1],center[label[0]])
            
            
    
    
    return center



Vec1Hot = WordVec1Hot(tfidf,idf,TopTF,testVec,article,No)
print(K_means(Vec1Hot,testVec))




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
    
Art = []
   
dk = wikipedia.page("Denmark")
Swe = wikipedia.page("Christianity")
dk = dk.content
Swe = Swe.content
dk = filter.remove_all_but_words(dk)
dk = filter.remove_stopwords(dk)
Swe = filter.remove_all_but_words(Swe)
Swe = filter.remove_stopwords(Swe)

Art.append(dk)
Art.append(Swe)

#print(len(tfidf[5]))

#print(TopTF[5]["varphi"])

def WordVec1Hot(tfidf,idf,TopTF,testVec, Art,No):
    n = len(tfidf) #Amount of clusters (aka amount of categories in MoD)
    m = No*len(TopTF) #Amount of words in our vocabulary
    ArtVecs = []
    
    for k in range(len(Art)):
        ArtVec = [0]*m
        for i in range(len(TopTF)):
            for j in range(len(TopTF[i])):
                if list(TopTF[i].keys())[j] in Art[k]:
                    ArtVec[j+i*No] = 1
                
        ArtVecs.append(ArtVec)
                
        
    return ArtVecs


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
        for j in range(0,N): #Change this when we have more than 1 article in ArtVec
            dist = {}
            for c in range(0,K):
                dist[c] = computeDist(ArtVec[j],center[c])
            label = computeLabel(ArtVec[j],center,dist)
            center[label[0]] = updateCenter(label[1],center[label[0]])
            
            if i == 100-1:
                cluster_lab.append(label)
            
            
            
    
    
    return [cluster_lab,center]



Vec1Hot = WordVec1Hot(tfidf,idf,TopTF,testVec,Art,No)
test = K_means(Vec1Hot,testVec)
print(test[0][1][0])
#print(K_means(Vec1Hot,testVec))




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
    
    
eps = 140
minPts = 2

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
#print(len(Art))
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


def RangeQuery(ArtVec,centerVec,eps):
    Neigh = []
    for i in range(len(ArtVec)):
        tempL = 0
        for j in range(len(ArtVec[i])):
           tempL += ((centerVec[j]-ArtVec[i][j])**2)**(0.5)
        if tempL <= eps:
            Neigh.append(i)
        #print(i, tempL)
    #print(derp/16)
    return Neigh

def DBSCAN(ArtVec,testVec,eps,minPts):
    label = [None] *len(ArtVec)
    C = 0
    for i in range(len(testVec)):
        Neigh = RangeQuery(ArtVec,testVec[i],eps)
        C = i
        expand(ArtVec,testVec[i],C,eps,minPts,label,Neigh)
    
    return label
        

def expand(ArtVec,testVec,C,eps,minPts,label,Neigh):
       # label[i] = C
        
        for j in Neigh:
            if label[j] == None:
                label[j] = C
            elif not (label[j] == None):
                continue
            
            label[j] = C
            #Neighj = RangeQuery(ArtVec,ArtVec[j],eps)
            #if len(Neighj) >= minPts:
             #   Neigh += Neighj
                    

ArtVecs = WordVec1Hot(tfidf,idf,TopTF,testVec,Art,No)
#print(len(ArtVecs))
DBLabel = DBSCAN(ArtVecs,testVec,eps,minPts)

print(*DBLabel, sep = " " )


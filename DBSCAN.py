import tf_idf_nocomm
import filter
import wikipedia

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
           if centerVec[j] != ArtVec[i][j] :
               tempL += 1
        tempL = tempL/len(ArtVec[i])
        if tempL <= eps:
            Neigh.append(i)
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
        
        for j in Neigh:
            if label[j] == None:
                label[j] = C
            elif not (label[j] == None):
                continue
            
            label[j] = C
            Neighj = RangeQuery(ArtVec,ArtVec[j],eps)
            if len(Neighj)*0.1 >= minPts:
                Neigh += Neighj
                    



import tf_idf_nocomm
import filter
import wikipedia

# Art = []

# dk = wikipedia.page("Denmark")
# Swe = wikipedia.page("Christianity")
# dk = dk.content
# Swe = Swe.content
# dk = filter.remove_all_but_words(dk)
# dk = filter.remove_stopwords(dk)
# Swe = filter.remove_all_but_words(Swe)
# Swe = filter.remove_stopwords(Swe)

# Art.append(dk)
# Art.append(Swe)



def generateBinaryWordMatrix(topword_matrix, number_of_topwords):
    testVec = []
    for i in range(len(topword_matrix)):
        temp = [0] * number_of_topwords * len(topword_matrix)
        for j in range(len(topword_matrix[i])):
            temp[j + i * number_of_topwords] = 1
        testVec.append(temp)
    return testVec



def WordVec1Hot(topword_matrix, testArticles,number_of_topwords):
    m = number_of_topwords*len(topword_matrix) #Amount of words in our vocabulary
    print("LENGTH", m)
    print("len(topword_matrix)", len(testArticles))
    ArtVecs = []

    for k in range(len(testArticles)):
        ArtVec = [0]*m
        for i in range(len(topword_matrix)):
            for j in range(len(topword_matrix[i])):
                if list(topword_matrix[i].keys())[j] in testArticles[k]:
                    ArtVec[j+i*number_of_topwords] = 1

        ArtVecs.append(ArtVec)

    return ArtVecs


def computeDist (point, center):
    EucDist = 0
    # print("hey1")
    for j in range(len(point)):
        EucDist += (point[j]-center[j])**2

    EucDist = EucDist**(0.5)

    return EucDist

def defineTFcenter(TopTF):
    center = []
    # print("hey2")
    for i in range(len(TopTF)):
        center.append(TopTF[i])

    return center

def computeLabel (ArtVec,center,dist):
    idx_min = min(dist,key= dist.get)
    # print("hey3")
    return [idx_min,ArtVec,center[idx_min]]

def updateCenter(cluster_lab,center):
    newCenter = [0]*len(center)
    # print("hey4")
    w_centers = 100  #Weight is 50 as the centers are built on a lot of articles
    for i in range(len(center)):
        # print(cluster_lab[i])
        newCenter[i] = (center[i]*0.98+cluster_lab[i]*0.02)

    return newCenter

def K_means(article_matrix, binary_word_matrix):
    # print("hey5")
    center = defineTFcenter( binary_word_matrix)
    label = []
    cluster_lab =[]
    N = len(article_matrix)
    K = len(center)

    for i in range(0,10):
        for j in range(0,N): #Change this when we have more than 1 article in article_matrix
            dist = {}
            print(j)
            for c in range(0,K):
                dist[c] = computeDist(article_matrix[j],center[c])
            label = computeLabel(article_matrix[j],center,dist)
            print(label[0])
            center[label[0]] = updateCenter(label[1],center[label[0]])

            if i == 10-1:
                cluster_lab.append(label)





    return cluster_lab



# Vec1Hot = WordVec1Hot(tfidf,idf,TopTF,testVec,Art,No)
# test = K_means(Vec1Hot,testVec)
# print(test[0][1][0])
#print(K_means(Vec1Hot,testVec))

import wikipedia
import nltk
from nltk.corpus import stopwords
from collections import defaultdict


stop = [x.lower() for x in stopwords.words('english')]
dklist  =[]
dk = wikipedia.page("Denmark")
dklist.append(dk.content.split(" "))
print(len(dklist[0]))
filtered_dklist = [w for w in dklist[0] if not w in stop]
print(len(filtered_dklist))



class WordCount:
    
    def __init__ (self,article):
        self.wordCounts = {}
        self.wikiArt = article
        self.wordCounts = defaultdict(int)
    
    def WordFreq(self):
        for word in self.wikiArt:
            if word in self.wikiArt:
                self.wordCounts[word] += 1
        return self.wordCounts
    
    def wcClassify(self, Categories):
        sortWC = sorted(self.wordCounts, key = self.wordCounts.get, reverse = True)
        Category = 0
        while Category == 0:
            for word in sortWC:
                if word in Categories:
                    Category = word
        return Category


wordC = WordCount(filtered_dklist)
print(wordC.WordFreq())
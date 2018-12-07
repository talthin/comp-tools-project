from collections import defaultdict
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
        Category = sortWC[1]
        return Category

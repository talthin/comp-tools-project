
class WordCount:
    
    def WordFreq(self, article):
        self.wordCounts = {}
        for word in article:
            if word in article:
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


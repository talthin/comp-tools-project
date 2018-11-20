from mrjob.job import MRJob
import os
from collections import defaultdict

freqWord = defaultdict(int)
class MRWordFrequencyCount(MRJob):

    def mapper(self,_,line):
        for word in line.split():
            yield word, 1

    def reducer(self,key,values):
        freqWord[key] = sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
    # print(freqWord)
    print(sorted(freqWord, key=freqWord.get, reverse=True))

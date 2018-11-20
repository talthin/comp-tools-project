from mrjob.job import MRJob
import os

SoW = ("Deer Bear River Car Car River Deer Car Bear", "Bear Antilope Stream River Stream")


class MRWordFrequencyCount(MRJob):
    
    def mapper(self,_,line): 
        for word in line.split(): ## THIS IS MAPREDUCE
            yield word, 1
        
    def reducer(self,key,values):
        yield key, sum(values)
        
if __name__ == '__main__':
    MRWordFrequencyCount.run()


#print(len(SoW))
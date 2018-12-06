# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:21:39 2018

@author: Frederik
"""

import matplotlib.pyplot as plt

plt.plot(KMacc)
plt.plot(DBacc)
plt.ylabel("Accuracy")
plt.xlabel("Amount of top words")
plt.show()

print(KMacc.index(max(KMacc))+8)
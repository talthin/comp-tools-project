import wikipedia
from collections import defaultdict
import filter
import wordCount

dk = wikipedia.page("Denmark")

dk = filter.remove_all_but_words(dk)
dk = filter.remove_stopwords(dk)

wc_dk = wordCount.wordFreq(dk)
print(wc_dk)
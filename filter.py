import re
import nltk
from nltk.corpus import stopwords


def remove_all_but_words(wordlist):
    filtered_wordlist = re.sub(r'[^a-zA-Z ]', '', wordlist).split()
    return filtered_wordlist


def remove_stopwords(wordlist):
    stop = [x.lower() for x in set(stopwords.words('english'))]
    filtered_wordlist = [w for w in wordlist if not w in stop]
    return filtered_wordlist



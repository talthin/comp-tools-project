import re
import nltk
from nltk.corpus import stopwords


### takes a string and removes digits and nonalpha characters
def remove_all_but_words(word_string):
    withoutTitles = re.sub(r'==.*==', '', word_string)
    filtered_wordlist = re.sub(r'[^a-zA-Z ]', '', withoutTitles).split()

    return filtered_wordlist

### takes a list of words and removes all stop words.
def remove_stopwords(wordlist):
    stop = [x.lower() for x in set(stopwords.words('english'))]
    filtered_wordlist = [w for w in wordlist if not w in stop]
    return filtered_wordlist

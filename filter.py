import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()

### takes a string and removes digits and nonalpha characters
def remove_all_but_words(word_string):
    withoutTitles = re.sub(r'==.*==', '', word_string)
    filtered_wordlist = re.sub(r'[^a-zA-Z ]', '', withoutTitles).split()

    return filtered_wordlist

### takes a list of words and removes all stop words.
def remove_stopwords(wordlist):
    # print(len(wordlist))
    stop = [x.lower() for x in set(stopwords.words('english'))]
    lowercase_wordlist = [lw.lower() for lw in wordlist]
    filtered_wordlist = [
        ps.stem(w) for w in lowercase_wordlist if not w in stop
    ]
    return filtered_wordlist

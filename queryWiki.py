import requests
import wikipedia
import filter
import wordCount
from collections import defaultdict

def getCategoryPageList(category, amount):

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        'action': "query",
        'list': "categorymembers",
        'cmtitle': "Category:" + category,
        'cmlimit': amount,
        'cmtype': "page",
        'format': "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    ### Get titles of wiki pages

    wikiTitles = []
    for i in range(len(DATA["query"]['categorymembers'])):
        wikiTitles.append(DATA["query"]['categorymembers'][i]['title'])
    return wikiTitles

def writeWikipageToFile(wikiTitles, filename):
    ### get single pages
    bigWordList = []
    for i in range(len(wikiTitles)):
        wikiPage = wikipedia.page(wikiTitles[i])
        wikiWordlist = filter.remove_all_but_words(wikiPage.content)
        cleanWikiWordlist = filter.remove_stopwords(wikiWordlist)
        for j in range(len(cleanWikiWordlist)):
            bigWordList.append(cleanWikiWordlist[j])

    ### write to file
    file = open(filename + ".txt", "w")

    for word in bigWordList:
        file.write(str(word) + " ")

    file.close()


import requests
import wikipedia
import filter
import wordCount
from collections import defaultdict

# Fetches a list of pages from wikipedia based on a category.
# Category is the category which you want pages from and amount is the number of pages you want from that category.
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

# removes symbols that are not words and stopwords
# page, the wikipage that you want to filter
def filterWikiData(page):
    wikiWordlist = filter.remove_all_but_words(page)
    cleanWikiWordlist = filter.remove_stopwords(wikiWordlist)
    return cleanWikiWordlist

# takes a list of titles and fetches the content of those pages from wikipedia and filters the data and writes it to a local file
# wikiTitles, the titles you want to fetch content from. filename, what you want the file to be namned
def writeWikipageToFile(wikiTitles, filename):
    ### get single pages
    bigWordList = []
    for i in range(len(wikiTitles)):
        wikiPage = wikipedia.page(wikiTitles[i])
        cleanWikiWordlist = filterWikiData(wikiPage.content)
        # wikiPage = wikipedia.page(wikiTitles[i])
        # wikiWordlist = filter.remove_all_but_words(wikiPage.content)
        # cleanWikiWordlist = filter.remove_stopwords(wikiWordlist)
        for j in range(len(cleanWikiWordlist)):
            bigWordList.append(cleanWikiWordlist[j])

    ### write to file
    file = open("wikidata/" + filename + ".txt", "w")

    for word in bigWordList:
        file.write(str(word) + " ")

    file.close()


# takes a list of titles and fetches the content of those pages from wikipedia and filters the data and converts it to a list
# wikiTitles, the titles you want to fetch content from. category, just for labeling the list. 
def createWikiList(wikiTitles, category):
    wikiList = []
    for i in range(len(wikiTitles)):
        bigWordList = []
        wikiPage = wikipedia.page(wikiTitles[i])
        cleanWikiWordlist = filterWikiData(wikiPage.content)
        for j in range(len(cleanWikiWordlist)):
            bigWordList.append(cleanWikiWordlist[j])
        wikiList.append([bigWordList, category])
    return wikiList


cat = "Historiography"
wikiTitles = getCategoryPageList(cat, 65)
wikilist = createWikiList(wikiTitles, cat)
writeWikipageToFile(wikiTitles, cat)

print(wikilist[1][1])


## TAKE TOP WORDS OUT OF EVERY CATEGORY
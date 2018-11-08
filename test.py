import urllib.request as ur
import urllib.parse
import json


baseurl = "http://en.wikipedia.org/w/api.php/?"
action = "action=query"
title = "titles=Denmark"
content = "prop=revisions&rvprop=content"
dataformat = "format=json"


query = "%s&%s&%s&%s&%s" % (baseurl, action, title, content, dataformat)

response = ur.urlopen(query)
html = response.read()
json_format = json.loads(html)
print(json_format)

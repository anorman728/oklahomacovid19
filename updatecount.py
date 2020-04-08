# Webscraping stuff
from bs4 import BeautifulSoup
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# I don't know why this works, but I get an SSL failure if I don't do it.

# JSON file stuff
import json

# Read existing data.
with open('covid19counts.json') as f:
    data = json.load(f)

url = 'https://coronavirus.health.ok.gov/'
content = urllib.request.urlopen(url)

htmlcontent = content.read()

soupObj = BeautifulSoup(htmlcontent, 'html.parser')

leftcolneeded = 'Positive (In-State)'

def findneededval():
    results = soupObj.find_all('tr')
    for el in results:
        children = iterabletolist(el.children)
        if children[1].text == leftcolneeded:
            return int(children[3].text.replace(',', ''))

def iterabletolist(iterableObj):
    # What a stupid anti-feature.
    returnList = []
    for el in iterableObj:
        returnList.append(el)

    return returnList


data.append(findneededval())

# Update count.
with open('covid19counts.json', 'w') as f:
    json.dump(data, f)

#find all links in a website click through
import requests
from bs4 import BeautifulSoup

#starting page below
getpage = requests.get('www.someurl.com')

linkList = []

webpages = []


getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

all_links= getpage_soup.findAll('a')

http = 'http'

for link in all_links:
#get all links from a webpage
    cleanLink = link.get('href')
    linkList.append(cleanLink)


for cleanLink in linkList:
#if type error is not put in, "none" will make this erroe come up "TypeError: argument of type 'NoneType' is not iterable"
#search thru page and find what has http. if it has this, and it is not in the list already, add to webpages.
#next go thru the ones in the list... 
    try:
        if http in cleanLink:
            if cleanLink not in webpages:
                webpages.append(cleanLink)
    except TypeError:
        continue

#next two loops are for going through each webpage from the initial starting page, and ultimately adding those that have http
for cleanLink in webpages:
    getOtherPage = requests.get(cleanLink)
    getOtherPage_soup= BeautifulSoup(getOtherPage.text, 'html.parser')
    continuedLinks = getOtherPage_soup.findAll('a')

    for link in continuedLinks:
        cleanedLink = link.get('href')
        if cleanedLink not in linkList:
            linkList.append(cleanedLink)



for cleanedLink in linkList:
    try:
        if http in cleanedLink:
            if cleanedLink not in webpages:
                webpages.append(cleanedLink)
    except TypeError:
        continue

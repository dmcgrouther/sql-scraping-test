#find all links in a website click through
import requests
from bs4 import BeautifulSoup

getpage = requests.get('https://www.games-workshop.com/en-US/Home')

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
            if cleanLink not it webpages:
                webpages.append(cleanLink)
    except TypeError:
        continue

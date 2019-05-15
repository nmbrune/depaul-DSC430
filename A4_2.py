# Nate Brune
# 3/5/2019 
# I have not given or received any unauthorized assistance on this assignment

'''
Below is the output of my script. I limited the links to active server pages (.aspx)
It checks 831 links and takes ~7 minutes to run.

[('the', 5546),
 ('and', 3489),
 ('of', 3135),
 ('to', 2894),
 ('in', 2720),
 ('a', 2575),
 ('students', 2187),
 ('for', 1593),
 ('is', 1292),
 ('or', 1277),
 ('with', 1098),
 ('be', 1002),
 ('will', 993),
 ('are', 982),
 ('course', 974),]
 '''

from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import re
import operator

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    # collect HTTP URLs from cdm.depaul.edu pages and limit responses to active server pages
                    if absolute[:26] == 'https://www.cdm.depaul.edu' and absolute[-4:] == 'aspx':
                        self.links.append(absolute)
                        
    
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links 


def getContent(url):
    '''takes in url and returns the content as a string'''
    response = urlopen(url)
    htmlSource = response.read()    
    response.close()
    content = htmlSource.decode().lower()
    return content
    
def getLinks(url):
    '''gets links from content'''
    linkContent = getContent(url)
    collector = Collector(url)
    collector.feed(linkContent)
    return collector.getLinks()

def wordDict(content):
    '''goes through content and pulls out all text then modifies the word dictionary'''
    global wDict
    pList = []
    paragraphs = re.findall(r'<p>(.*?)</p>',str(content))
    for p in paragraphs:
        pList += p.split(' ')
    headers = re.findall(r'<h2>(.*?)</h2>',str(content))
    for h in headers:
        pList += h.split(' ')

    for x in pList:
        if x in wDict:
            wDict[x] += 1
        elif x not in wDict:
            wDict[x] = 1


#declaring variables
wDict = {}
linksGathered, linksCalled, linksErr = [], [], []

#gets content from first link then gathers all links from that page
baseurl = 'https://www.cdm.depaul.edu'
links = getLinks(baseurl)
linksCalled.append(baseurl)
wordDict(getContent(baseurl))

for link in links:
    if link not in linksGathered:
        linksGathered.append(link)

#recursively runs the functions for all links gathered
#handles for errors with web page
for url in linksGathered:
    if url not in linksCalled:
        try:
            links = getLinks(url)
            linksCalled.append(url)
            wordDict(getContent(url))
        except:
            linksErr.append(url)
        for link in links:
            if link not in linksGathered:
                linksGathered.append(link)

top15 = sorted(wDict.items(), key=operator.itemgetter(1), reverse=True)[:25]
print(top15)



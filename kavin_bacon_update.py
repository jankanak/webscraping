from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 
import datetime
import random

random.seed(datetime.datetime.now())

def getlinks(getarticle):
    html=urlopen('https://en.wikipedia.org/'+getarticle)
    bsobj=BeautifulSoup(html,'lxml')
    return bsobj.find("div",{"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links=getlinks('wiki/Kevin_Bacon')
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getlinks(newArticle)
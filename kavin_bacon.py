from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsobj=BeautifulSoup(html,'lxml')

for link in bsobj.find("div",{"id":"bodyContent"}).find_all("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
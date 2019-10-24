from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

html=urlopen('https://pythonscraping.com/pages/page3.html')
bsobj=BeautifulSoup(html,'lxml')

#for child in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
for name in bsobj.find_all("tr",class_="gift"):
    print(name.text)

images=bsobj.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])

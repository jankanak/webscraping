from urllib.request import urlopen 
from bs4 import BeautifulSoup
kanak=urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
kan=BeautifulSoup(kanak.read(),'html.parser')
bs=kan.findAll("span",{"class":"green"})
for name in bs:
    print( name.get_text())





""" 
from urllib.error import HTTPError
from urllib.error import URLError
try:
    kanak=urlopen("https://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
       print("the server is not found")
else:
    print("no error found")
"""
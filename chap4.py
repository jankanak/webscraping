from urllib.request import urlopen 
from bs4 import BeautifulSoup
kanak=urlopen("http://quotes.toscrape.com")
kan=BeautifulSoup(kanak.read(),'html.parser')
print(kan)
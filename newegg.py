from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://www.newegg.com/p/pl?Submit=StoreIM&Depa=10&Category=354')
soup=BeautifulSoup(html,'html.parser')
print(soup)
# for item in bsobj.find_all('div',class_='item-container'):
#     print(len(item))

# for item in soup.findAll('div',class_='item-container'):
#     for title in item.find('a',class_='item-title'):
#         print(title.text)
# item=bsobj.find('div',class_='item-container')
# print(item)
# containers=soup.find_all('div',class_='item-container')
# for container in containers:
#     brand=container.div.div.a.img['title']
#     print(brand)
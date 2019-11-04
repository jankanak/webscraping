from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv

url=('https://www.goodreads.com/quotes?page=')
current_page=1

csv_file=open('quotes100.csv','w',encoding='utf-8')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Quotes'])

while current_page<101:
    main_url=url+str(current_page)
    html=urlopen(main_url)
    so=html.read()
    soup=BeautifulSoup(so,'lxml')
    try:
        for qu in soup.findAll('div',class_='quote'):
            quo=qu.find('div',class_='quoteDetails')
            quotes=qu.find('div',class_='quoteText').contents[0].strip()
            # print(quotes.strip())
            # print('\n')
            csv_writer.writerow([quotes])
    except:
        None
    current_page+=1
    

    # quo=qu[1]
    # quot=quo.contents[3]
    # quote=quot.contents
    # print(quote)

  

# soup=BeautifulSoup(url,'lxml')
# print(soup)
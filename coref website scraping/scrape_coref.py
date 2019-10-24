from bs4 import BeautifulSoup
import requests
import csv

source=requests.get("https://coreyms.com").text
soup=BeautifulSoup(source,'lxml')

csv_file=open('kanak1.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Title','Published Date','Summary','Youtube Link'])

for article in soup.find_all('article'):
    headline=article.h2.a.text
    print(headline)
    time=article.find('time',class_='entry-time').text
    print(time)
    summary=article.find('div',class_='entry-content').p.text
    print(summary)
    try:
        vid_id=article.find('iframe',class_='youtube-player')['src'].split('/')[4].split('?')[0]
        y_link=f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        y_link=None
    print(y_link)
    csv_writer.writerow([headline,time,summary,y_link])
csv_file.close()
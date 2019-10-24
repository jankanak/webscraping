from bs4 import BeautifulSoup
import requests

source=requests.get("http://coreyms.com").text
soup=BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    for youtube in article.find('span',class_='embed-youtube'):
    # headline=article.h2.a.text
    # print(headline)
    # summary=article.find('div',class_='entry-content').p.text
    # print(summary)
        if 'iframe'==True:
            vid_id=youtube.find('iframe',class_='youtube-player')['src']
            vid_id=vid_id.split('/')[4]
            vid_id=vid_id.split('?')[0]
            y_link=f'https://www.youtube.com/watch?v={vid_id}'
            print(y_link)
    #print("\n")
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv 
source=urlopen('http://coreyms.com')
soup=BeautifulSoup(source,'lxml')
csv_file=open('ka.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary'])
for s1 in soup.find_all('article'):
    
    headline=s1.h2.a.text
    print(headline)
    summary=s1.find('div',class_="entry-content").p.text
    print(summary)
    vid_src=s1.find('iframe',class_="youtube-player")['src']
    vid_id=vid_src.split('/')[4]
    vid_id=vid_id.split('?')[0]
    print()
    csv_writer.writerow([headline,summary])
csv_file.close()

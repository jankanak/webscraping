from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv 
source=urlopen('http://coreyms.com')
soup=BeautifulSoup(source,'lxml')
csv_file=open('kanak.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary'])
for s1 in soup.find_all('article'):
    
    headline=s1.h2.a.text
    print(headline)
    summary=s1.find('div',class_="entry-content").p.text
    print(summary)
    csv_writer.writerow([headline,summary])
csv_file.close()

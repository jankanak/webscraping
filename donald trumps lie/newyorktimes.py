from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

records=[]
source=urlopen('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
bsobj=BeautifulSoup(source,'html.parser')
for first in bsobj.find_all('span',class_='short-desc'):
    date=first.contents[0].text[0:-1]+', 2017'
    lie=first.contents[1][1:-1]
    explanation=first.contents[2].text[1:-1]
    link=first.find('a')['href']
    #print(date.text)
    #print(lie[1:-1])
    #print(muted_tag.text[1:-1])
    #print(link)
    records.append((date,lie,explanation,link))

    frame=pd.DataFrame(records,columns=['Date','Trump`s Lie','Explanation','link'])
    frame.to_csv('trump_lies.csv',encoding='utf-8')


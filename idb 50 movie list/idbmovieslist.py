from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd 
records=[]
html=urlopen('https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc')
soup=BeautifulSoup(html,'html.parser')
for oneelement in soup.find_all('div',class_='lister-item mode-advanced'):
    element=oneelement.contents[5]
    name_movie=element.contents[1].a.text
    movie=name_movie
    year=element.find('span',class_='lister-item-year text-muted unbold')
    year=year.text[1:-1]
    duration=element.find('span',class_='runtime').text
    rate=element.contents[5]
    rating=rate.find('strong')
    rating=rating.text
    try:
        metascore=element.find('span',class_='metascore favorable')
        metascore=metascore.text
        #print(metascore.text)
    except:
        None
    description=element.contents[7].text[5:]
    #print(description)
    prod=element.contents[9]
    producer=prod.contents[1].text
    #print(producer)
    starring=element.find('p',class_="")
    stars=starring.find_all('a')
    # for p in {star for star in stars[1:]}:
    #     po=p.text
    #     print(po)
    incomevotes=element.contents[11]
    try:
        votes=incomevotes.contents[3].text
        votes=votes
        #print(votes)
    except:
        None
    
    try:
        income=incomevotes.contents[9].text
        income=income
        #print(income)
    except:
        None
    records.append((movie,year,duration,rating,metascore,description,producer,votes,income))
    frame=pd.DataFrame(records,columns=['Movie Name','Release Year','Duration','Rating','Metascore','Description','Producer','Votes','Income'])
    frame.to_csv('idbmovie50list.csv',encoding='utf-8')
   
    print("\n")
    # print('List:')
    # print(i)
    # print("---------------------------------------------------------------------------------")
    # print(oneelement.h3.a.text)#name of the movie
    # print(oneelement.find('span',class_='runtime').text)#duration of the movie
    # print(oneelement.find('div',class_="inline-block ratings-imdb-rating").text)
    # director=oneelement.find('div',class_='lister-item-content')#director of the movie
    #print(director.find('p',class_="").a.text)
    # starring=director.find('p',class_="")
    # stars=starring.find_all('a')
    # for p in {star for star in stars[0]}:
    #     print("producer:"+p)
    #actor/Actress
    #print("Actor/Actress:")
    # for p in {star for star in stars[1:]}:
    #     print(p.text)

    # ##votes 
    # try:
    #     for po in oneelement.find_all('span', attrs={'name' : 'nv'})[0]:
    #         print(po)
    # except:
    #     None
    
    # # #income 
    # try:
    #     for po in oneelement.find_all('span', attrs={'name' : 'nv'})[1]:
    #         print(po)
    # except:
    #     None
    
    # print("\n")
    # i=i+1
   
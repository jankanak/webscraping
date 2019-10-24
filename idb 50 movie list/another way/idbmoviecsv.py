from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
html=urlopen('https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc')
soup=BeautifulSoup(html,'html.parser')
i=1
for oneelement in soup.find_all('div',class_='lister-item mode-advanced'):
    movie_name=oneelement.h3.a.text#name of the movie
    movie_duration=oneelement.find('span',class_='runtime').text#duration of the movie
    ratings=oneelement.find('div',class_="inline-block ratings-imdb-rating").text
    director=oneelement.find('div',class_='lister-item-content')#director of the movie
    #print(director.find('p',class_="").a.text)
    starring=director.find('p',class_="")
    stars=starring.find_all('a')
    for p in {star for star in stars[0]}:
        direc=p
    #actor/Actress
    for pt in {star for star in stars[1:]}:
        actor=pt.text
        print(actor)

    ##votes 
    try:
        for po in oneelement.find_all('span', attrs={'name' : 'nv'})[0]:
            votes=po
    except:
        None
    # #income 
    try:
        for pot in oneelement.find_all('span', attrs={'name' : 'nv'})[1]:
            income=pot
    except:
        None

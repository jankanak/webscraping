from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc')
soup=BeautifulSoup(html,'html.parser')
i=1
for oneelement in soup.find_all('div',class_='lister-item mode-advanced'):
    print('List:')
    print(i)
    print("---------------------------------------------------------------------------------")
    print(oneelement.h3.a.text)#name of the movie
    print(oneelement.find('span',class_='runtime').text)#duration of the movie
    print(oneelement.find('div',class_="inline-block ratings-imdb-rating").text)
    director=oneelement.find('div',class_='lister-item-content')#director of the movie
    #print(director.find('p',class_="").a.text)
    starring=director.find('p',class_="")
    stars=starring.find_all('a')
    for p in {star for star in stars[0]}:
        print("producer:"+p)
    #actor/Actress
    print("Actor/Actress:")
    for p in {star for star in stars[1:]}:
        print(p.text)

    ##votes 
    try:
        for po in oneelement.find_all('span', attrs={'name' : 'nv'})[0]:
            print(po)
    except:
        None
    
    # #income 
    try:
        for po in oneelement.find_all('span', attrs={'name' : 'nv'})[1]:
            print(po)
    except:
        None
    
    print("\n")
    i=i+1
   
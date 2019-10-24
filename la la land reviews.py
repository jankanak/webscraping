from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html=urlopen('https://www.rottentomatoes.com/m/la_la_land/reviews?type=top_critics')
bsobj=BeautifulSoup(html,'lxml')
csv_file=open('lalaland5.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Name','Published Date','review'])

rev_table=bsobj.findAll('div',class_='row review_table_row')
for name in rev_table:
    name1=name.find('div',class_='col-sm-13 col-xs-24 col-sm-pull-4 critic_name')
    #print(name.find('a')['href']) 
    name2=name1.find('a',class_='unstyled bold articleLink')
    p=name2.text
    review=name.find('div',class_='the_review').text
    comment_date=name.find('div',class_='review-date subtle small')
    q=comment_date.text
    # print("\n")
    csv_writer.writerow([p,review,q])
csv_file.close()
  
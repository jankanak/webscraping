from bs4 import BeautifulSoup
from urllib.request import urlopen

html=urlopen('https://www.espn.com/nba/stats/player')
bsobj=BeautifulSoup(html,'html.parser')
record=[]
table=bsobj.find('tbody',class_='Table__TBODY')
for name in table.find_all('tr',class_='Table__TR Table__TR--sm Table__even'):
    print(name.a.text)
# for table_data in table.find_all('tr',class_='Table__TR Table__TR--sm Table__even'):
#     position=table_data.contents[0].text
#     PTS=table_data.contents[3].text
#     record.append((position,PTS))
# print(record)
#print((table_data))
    
# position=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[0]
# gp=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[1]
# Min=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[2]
# PTS=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[3]
# FGM=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[4]
# FGA=table.find('tr',class_='Table__TR Table__TR--sm Table__even').contents[5]

# # #position=table_data.contents[0]
# print(position.text)
# print(gp.text)
# print(Min.text)
# print(PTS.text)
# print(FGM.text)
# print(FGA.text)
#print(len(table))



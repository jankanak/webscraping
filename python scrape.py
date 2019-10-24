
from urllib.request import urlopen
from bs4 import BeautifulSoup

weather=urlopen("https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XKdyiFUzZ0w")
wea=BeautifulSoup(weather,'html.parser')
we=wea.find(id="seven-day-forecast-list")
wed=we.findAll(class_="tombstone-container")
#items=wed.find_all(class_="period-name")
period_names=[item.find(class_="period-name").get_text() for item in wed]
short=[item.find(class_="short-desc").get_text() for item in wed]
temp=[item.find(class_="temp").get_text() for item in wed]
print(period_names)
print(short)
print(temp)

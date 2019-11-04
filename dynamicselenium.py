import pandas as pd
from selenium import webdriver
import requests
import time 
time.sleep(3)
import csv

max_page=5
max_index=3
driver=webdriver.Firefox(executable_path="G:\gecodriver\geckodriver.exe")

# driver.get('http://econpy.pythonanywhere.com/ex/001.html')
# buyers=driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices=driver.find_elements_by_xpath('//span[@class="item-price"]')
# number_of_items=len(buyers)
# for i in range(number_of_items):
#     print(buyers[i].text+":"+prices[i].text)
# csv_file=open('quotes100.csv','w',encoding='utf-8')
# csv_writer=csv.writer(csv_file)
# csv_writer.writerow(['Buyers','Prices']

for i in range(1,max_page+1):
    page_number=2*"0"+str(i)
    #(max_index-len(str(i)))
    url='http://econpy.pythonanywhere.com/ex/'+page_number+'.html'
    driver.get(url)
    buyers=driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    #print(buyers.text)
    prices=driver.find_elements_by_xpath('//span[@class="item-price"]')
    number_of_items=len(buyers)
    with open('dynamicdata5.csv','a') as f:
        for i in range(number_of_items):
            f.write(buyers[i].text+" " + " : ")
            f.write(prices[i].text)
            f.write("\n")
    # print(page_number)


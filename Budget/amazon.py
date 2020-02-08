from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import re

class AmazonBot(object):
    def __init__(self,items):
        self.amazon_url="https://www.amazon.in/"
        self.items=items
        self.driver=webdriver.Chrome("C:/Users/SunMoon Computer/Desktop/Automation/chromedriver.exe")
        self.driver.get(self.amazon_url)
        
    def search_items(self):
        urls=[]
        prices=[]
        names=[]
        for item in self.items:
            print(f"searching for {item}")

            input_search=self.driver.find_element_by_id("twotabsearchtextbox").send_keys(item)
            time.sleep(3)
            button_search=self.driver.find_element_by_class_name("nav-input").click()
            time.sleep(3)
            first_search=self.driver.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[4]/div[1]/div[1]")
            time.sleep(3)
            asin=first_search.get_attribute("data-asin")
            url="https://www.amazon.in/dp/"+asin
            price=self.get_product_price(url)
            name=self.get_product_name(url)
            prices.append(price)
            names.append(name)
            urls.append(url)
            print(name)
            print(price)
            print(url)
        return names,prices,urls
    
    def get_product_name(self,url):
        self.driver.get(url)
        try:
            product_name=self.driver.find_element_by_id("productTitle").text
        except:
            pass
        if product_name==None:
            product_name="Not available"
        return product_name
    
    def get_product_price(self,url):
        self.driver.get(url)
        try:
            product_price=self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass
        if product_price==None:
            product_price="Not available"
        return product_price
    


items=["toothpastes"]
amazon=AmazonBot(items)
amazon.search_items()
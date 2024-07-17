from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv
import os

driver=webdriver.Chrome()
driver.get("https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin")
sleep(10)
page=driver.page_source
soup=BS(page,'lxml')
content=soup.find('ul',class_='ubsf_sitemap-list')
restaurents_list= content.find_all('div',class_='ubsf_sitemap-location-address')
# print(restaurents_list)
# print(page)


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "BurgerWars")
file_path = os.path.join(desktop_path, "restaurant.csv")
with open(file_path,mode='a',newline='') as outputFile:
    restaurentCSV= csv.writer(outputFile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    restaurentCSV.writerow(['restaurent','street','zip','city','country'])
    restaurents='McDonalds'
    city='paris'
    country= 'London'

    for restaurent in restaurents_list:
        street= restaurent.text.split(",")[0]
        zipcode=restaurent.text.split(",")[1][1:6]
        restaurentCSV.writerow([restaurents,street,zipcode,city,country])
    
driver.close()



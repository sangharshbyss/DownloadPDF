#!usr/bin/env python3
import urllib
import re
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
#set chrome options for automatic download without popup.
chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": '/home/sangharsh/Download',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)

driver = webdriver.Chrome(options = chrome_options)


webpage = r"https://documents.un.org/prod/ods.nsf/home.xsp"  # this will be constant

#set variable to enter in search box
searchterm = "A/HRC/41/4"  # this will be constant - fon now

#open the webpage with get command
driver.get(webpage)
time.sleep(3)

#find the element "symbol", insert data and click submit.
symbolBox = driver.find_element_by_id("view:_id1:_id2:txtSymbol")
symbolBox.send_keys(searchterm)
submit = driver.find_element_by_id("view:_id1:_id2:btnRefine")
submit.click()
'''
with help from https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/
and https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all and https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
'''
#the data will be handed over to beautifulsoup. grap links with helpf of regX
soup_level1=BeautifulSoup(driver.page_source, 'lxml')
#creating empty list for future use
links = []
x = 0 #this will work as counter in if loop
#find report link with help of regX, and list all links containing the 'dcouments' words in link
#all links to the reports have this word.
listOfLinks= soup_level1.find_all('a', href = re.compile("documents"))
print ('page parsing')
print (*listOfLinks, sep="\n")
# iterate over all the links stored in listOfLinks
for result in listOfLinks:
    if x <= 6:
        link = listOfLinks[x]
        print ('links to click')
        print (link)
        clickLink = link['href']
        download = driver.get(clickLink)
        x += 1

driver.close()
#recursive level 2. click on each link


'''
button_click= driver.find_element_by_partial_link_text("Research")
datalist = [] #empty list
x = 0 #counter

for link in soup_level1.find_all('a', text=re.compile("Results:")):
    link = button_click


#list of search results open up and 1st occarance is clicked by coppying its id element
downloadPage = driver.find_element_by_id("view:_id1:_id2:cbMain:_id135:rptResults:0:linkURL")
downloadPage.click()
time.sleep(10)
driver.quit()
'''
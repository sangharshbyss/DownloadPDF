import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
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


webpage = r"https://documents.un.org/prod/ods.nsf/home.xsp"  # edit me
#set variable to enter in search box

searchterm = "A/HRC/41/5"  # edit me

#open the webpage with get command
driver.get(webpage)
time.sleep(3)

#find the element "symbol", insert data and click submit.
symbolBox = driver.find_element_by_id("view:_id1:_id2:txtSymbol")
symbolBox.send_keys(searchterm)
submit = driver.find_element_by_id("view:_id1:_id2:btnRefine")
submit.click()
#list of search results open up and 1st occarance is clicked by coppying its id element
downloadPage = driver.find_element_by_id("view:_id1:_id2:cbMain:_id135:rptResults:0:linkURL")
downloadPage.click()
time.sleep(10)
driver.quit()
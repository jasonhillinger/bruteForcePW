# Required Packages
# pip3 install selenium
# pip3 install webdriver-manager

from pickle import FALSE, TRUE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = 'D:\pythonBot\login.html'
USERNAME = 'jason123'
PASSWORD = ''

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #keeps window open option

#opening window
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options = options, service=s)
#driver.maximize_window()
driver.get(URL)   #url to be opened

time.sleep(2)

USERNAMEin = driver.find_element_by_xpath('/html/body/main/form/input[1]')
USERNAMEin.send_keys(USERNAME)

PASSWORDin = driver.find_element_by_xpath('/html/body/main/form/input[2]')

SUBMIT = driver.find_element_by_xpath('//*[@id="login-form-submit"]')

# SUCCESS = driver.find_element_by_xpath('/html/body/h1')
running = TRUE
i = -1
while running:
    i = i+1
    PASSWORD = str(i)
    try:
        driver.execute_script("arguments[0].value = ''",PASSWORDin) #empties the field for a new password to be inputed
        PASSWORDin.send_keys(PASSWORD)                              #inputs new password attempt
        SUBMIT.click()
        print(PASSWORD)
    except:
        i= i-1                                                      #reversing iteration due to exception being caught
        PASSWORD = str(i)
        running = FALSE
        print("Password for account " + USERNAME + " is " + PASSWORD)
        break

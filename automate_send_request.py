from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.action_chains import ActionChains
from sqlalchemy.engine import create_engine
import random
from selenium.webdriver.common.alert import Alert 
import pandas as pd
from pyzbar.pyzbar import decode
from PIL import Image
#Run on already opened browser
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9250")
chrome_driver = "D:\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
#driver.find_element_by_xpath("//span[@class='artdeco-pill__text'][text()[contains(.,'Post')]]").click()
time.sleep(3)
# driver.find_element_by_xpath("//input[@class='search-global-typeahead__input always-show-placeholder']").send_keys('hcl')
# driver.find_element_by_xpath("//input[@class='search-global-typeahead__input always-show-placeholder']").send_keys(Keys.ENTER)
# time.sleep(5)
# driver.find_element_by_xpath("//span[@class='artdeco-button__text'][text()[contains(.,'People')]]").click()   
# time.sleep(5)

Flag=True
def test_function():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(3)
    for i in driver.find_elements_by_xpath("//button[text()[contains(.,'Connect')]]"):
        print(len(driver.find_elements_by_xpath("//button[text()[contains(.,'Connect')]]")))
        time.sleep(2)
        if(i.is_displayed()):
            time.sleep(2)
            i.click()
            time.sleep(2)
            driver.find_element_by_xpath("//button[@aria-label='Send now']").click()
            time.sleep(2)
    driver.find_element_by_xpath("//span[@class='artdeco-button__text'][text()[contains(.,'Next')]]").click()
    time.sleep(2)

while Flag:
    test_function()
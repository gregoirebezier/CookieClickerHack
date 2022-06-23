#!/usr/bin/python3
from selenium import webdriver
from time import sleep
from decouple import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
import warnings


###---------REMOVE THE DEPRECATIONWARNING---------###
warnings.filterwarnings("ignore", category=DeprecationWarning)

def ClickCookie():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.set_page_load_timeout(30)

###---------MAXIMIZE WINDOW---------###
    driver.maximize_window()
    driver.find_element_by_id("langSelect-FR").click()
    sleep(3)
    tempVar = 0
###---------CHEAT CODE---------###
    #execute cheat code script in console js
    #driver.execute_script("Game.Earn(999999999999999999999999999999999)")
    #sleep(5)
    #driver.find_element_by_id("storeBulk100").click()
    while (1):
        driver.find_element_by_id("bigCookie").click()
        Products = driver.find_elements_by_xpath("//*[@class='product unlocked enabled']")
        craftObject = driver.find_elements_by_xpath("//*[@class='crate upgrade enabled']")
        lenghtProduct = len(Products)
        lenghtCraft = len(craftObject)
        try:
            while (lenghtCraft > tempVar):
                try:
                    craftObject[tempVar].click()
                except:
                    pass
                tempVar += 1
        except:
            pass
        tempVar = 0
        try:
            Products[lenghtProduct-1].click()
        except:
            pass
    print("prog stop")

def main():
    driver = ClickCookie()

main()
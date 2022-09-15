#!/usr/bin/python3
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import warnings
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


###---------REMOVE THE DEPRECATIONWARNING---------###
warnings.filterwarnings("ignore", category=DeprecationWarning)

def ClickCookie():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.set_page_load_timeout(30)

###---------MAXIMIZE WINDOW---------###
    driver.maximize_window()
    sleep(2)
    try:
        driver.find_element(By.ID, "langSelect-FR").click()
    except:
        pass
    sleep(3)
    tempVar = 0
###---------CHEAT CODE---------###
    #execute cheat code script in console js
    driver.execute_script("Game.Earn(99999999999999999999999999)")
    sleep(5)
    driver.find_element(By.ID, "storeBulk100").click()
    while (1):
        driver.find_element(By.ID, "bigCookie").click()
        Products = driver.find_elements(By.XPATH, "//*[@class='product unlocked enabled']")
        craftObject = driver.find_elements(By.XPATH, "//*[@class='crate upgrade enabled']")
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
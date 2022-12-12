# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:17:41 2022

@author: Sachin Kansal
"""

#google timer scrapping


from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

xpath='//*[@id="act-timer-section"]/div/div[1]/div'
Options= webdriver.ChromeOptions()
Options.add_argument("Headless")
driver= webdriver.Chrome(executable_path='./chromedriver',options=Options)
#adress='https://www.google.com/search?q=timer&sxsrf=ALiCzsY3b4kkqzU7MYEVd70tmWmCGo7HWQ%3A1670784400661&source=hp&ei=kCWWY6uhJv6MseMP6fSwmAU&iflsig=AJiK0e8AAAAAY5YzoBb0CwKaoe4WUgNcZ8Ra2T8R79Wi&ved=0ahUKEwirqcj1nPL7AhV-RmwGHWk6DFMQ4dUDCAk&uact=5&oq=timer&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEEMyBAgAEEMyBAgAEEMyCwguEIAEEMcBENEDMgsILhCABBDHARCvATIECAAQQzINCAAQgAQQsQMQgwEQCjIFCAAQgAQyBQgAEIAEMgsILhCABBDHARDRAzoECCMQJzoKCAAQsQMQgwEQQzoECC4QQzoFCAAQkQI6BwgAELEDEEM6BwguELEDEEM6CAgAEIAEELEDUABYwCJgmyRoAHAAeACAAdwBiAH5BJIBBTAuMy4xmAEAoAEB&sclient=gws-wiz'
minutes=input("please enter the time in minutes")
adress='https://www.google.com/search?q='+minutes+'+minute+timer&sxsrf=ALiCzsYfF0BVxgo23yH33f9py5Z6s5cBCg%3A1670785702895&ei=piqWY6anNruTseMPzLiS6Ak&oq=6+timer&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIICAAQBxAeEAoyBggAEAcQHjoKCAAQRxDWBBCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFDTF1jlGGCWJGgBcAF4AIABgwGIAfQBkgEDMC4ymAEAoAEByAEKwAEB&sclient=gws-wiz-serp'
driver.get(adress)

wait=WebDriverWait(driver, 10)

wait.until(ec.visibility_of_element_located((By.XPATH,xpath)))

element = driver.find_element(By.XPATH,xpath)

while element.text != '0s':
    element = driver.find_element(By.XPATH,xpath)
    print(element.text)
    time.sleep(1)

driver.close()

from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('http:\\ya.ru')
searchString= browser.find_element_by_id('text')
searchString.send_keys('QA NINJAS')
searchString.submit()
time.sleep(3)
browser.quit()

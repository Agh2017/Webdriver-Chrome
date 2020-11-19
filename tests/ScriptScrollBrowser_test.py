from selenium import webdriver
import time

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    button= browser.find_element_by_tag_name('button')
    #scroll 100px down
    browser.execute_script('window.scrollBy(0, 100);')
finally:
    time.sleep(10)
    browser.quit()

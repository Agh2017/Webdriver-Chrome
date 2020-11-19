from selenium import webdriver
import time

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);')
finally:
    time.sleep(10)
    browser.quit()

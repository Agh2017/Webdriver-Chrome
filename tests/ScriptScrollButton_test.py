from selenium import webdriver
import time

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    button= browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
finally:
    time.sleep(10)
    browser.quit()

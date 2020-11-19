# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")
# time.sleep(3)
# browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    time.sleep(3)
    browser.quit()

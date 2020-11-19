from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.implicitly_wait(5)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    message = browser.find_element_by_id("price")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_id('book')
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'100'))
    button.click()
    x = browser.find_element_by_id('input_value')
    valueX= int(x.text)
    y = calc(valueX)
    inputAnswer = browser.find_element_by_id('answer')
    inputAnswer.send_keys(str(y))
    button2 = browser.find_element_by_css_selector('button[type="submit"]')
    button2.click()



finally:
    time.sleep(5)
    browser.quit()

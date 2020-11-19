from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button1 = browser.find_element_by_css_selector('button[type="submit"]')
    button1.click()
    confirm1 = browser.switch_to.alert
    confirm1.accept()
    x = browser.find_element_by_id('input_value')
    valueX= int(x.text)
    y = calc(valueX)
    inputAnswer = browser.find_element_by_id('answer')
    inputAnswer.send_keys(str(y))
    button2 = browser.find_element_by_css_selector('button[type="submit"]')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()

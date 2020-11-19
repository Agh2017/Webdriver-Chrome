from selenium import webdriver
import math,time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    img=browser.find_element_by_css_selector('img#treasure')
    numberTreasure = img.get_attribute('valuex')
    y=calc(numberTreasure)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button[type='submit'].btn")
    checkbox1 = browser.find_element_by_id('robotCheckbox')
    checkbox1.click()
    radiobutton1 = browser.find_element_by_id('robotsRule')
    radiobutton1.click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()
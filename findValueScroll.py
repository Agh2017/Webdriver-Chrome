from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:

    browser.get(link)
    element1 = browser.find_element_by_id('input_value')
    value1 = element1.text
    y = calc(value1)
    browser.execute_script('window.scrollBy(0, 100);')
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button[type='submit'].btn")
    checkbox1 = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    checkbox1.click()
    radiobutton1 = browser.find_element_by_css_selector('label[for="robotsRule"]')
    radiobutton1.click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()


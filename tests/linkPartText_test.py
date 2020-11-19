from selenium import webdriver
import time

link = "https://www.degreesymbol.net/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element_by_partial_link_text("examples")
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
from selenium import webdriver
import random, string, time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    #find all elements with type='text'
    elements = browser.find_elements_by_css_selector("[type='text']")
    letters = string.ascii_lowercase
    #filling
    for element in elements:
       element.send_keys(''.join(random.choice(letters) for _ in range(8)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time
link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    value1 = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    value2 = int(num2.text)
    summ = value1+value2
    print(summ)
    select1 = Select(browser.find_element_by_css_selector('select#dropdown'))
    select1.select_by_value(str(summ))
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

# способы с 2-мя кликами
#browser.find_element_by_tag_name("select").click()
#browser.find_element_by_css_selector("option:nth-child(2)").click()
#browser.find_element_by_css_selector("[value='1']").click()
# способы с 1-м кликом

#select = Select(browser.find_element_by_tag_name("select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"
#Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

#Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1), так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".

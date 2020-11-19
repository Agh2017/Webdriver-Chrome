from selenium import webdriver
import os, time

link = 'http://suninjuly.github.io/file_input.html'
browser=webdriver.Chrome()

try:
    browser.get(link)
    inputName = browser.find_element_by_css_selector('input[name="firstname"]')
    inputName.send_keys('Ya')
    inputLastName = browser.find_element_by_css_selector('input[name="lastname"]')
    inputLastName.send_keys('SoYa')
    inputEmail = browser.find_element_by_css_selector('input[name="email"]')
    inputEmail.send_keys('SoYa@YA.BOP')
    inputFile = browser.find_element_by_id('file')
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, '333.txt')
    inputFile.send_keys(file_path)
    button = browser.find_element_by_css_selector('button[type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()

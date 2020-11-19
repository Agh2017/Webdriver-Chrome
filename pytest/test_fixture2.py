# Не забудьте указать параметр -s, чтобы увидеть текст, который выводится командой print().
# pytest -s -v test_fixture2.py
from selenium import webdriver
import pytest

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
    print('\nstsrt browser for test..')
    browser = webdriver.Chrome()
    yield browser #код выполнится после окончания тестов
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

class TestMainPage1:
    #вызываем фикстуру передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')

    def test_quest_should_see_login_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

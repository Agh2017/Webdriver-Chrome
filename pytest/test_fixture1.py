# Не забудьте указать параметр -s, чтобы увидеть текст, который выводится командой print().
# pytest -s test_fixture1.py
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self): #запускает браузер 1 раз на оба теста
        print("\nstart browser for test suite 1 ..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self): #закрывает браузер 1 раз
        print("quit browser for test suite 1 ..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self): #запускает браузер 2 раза, по 1 на каждый тест
        print("start browser for test 2..")
        self.browser = webdriver.Chrome()

    def teardown_method(self): #закрывает браузер 2 раза
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
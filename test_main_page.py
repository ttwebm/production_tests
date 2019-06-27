# import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def ttest_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем
    # в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()
    # time.sleep(30)

def ttest_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

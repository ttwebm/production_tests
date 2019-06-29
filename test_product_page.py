import time
import pytest
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}"
urls = [url.format(i) for i in range(10)]
# urls = [url.format(0)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.get_product_name_and_price()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_messages_about_adding()
    page.should_be_correct_product_name_and_price()


def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    # check with is_not_element_present
    page.should_not_be_success_message_1()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    # check with is_not_element_present
    page.should_not_be_success_message_1()


def test_message_dissapeared_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    # check with is_disappeared
    page.should_not_be_success_message_2()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart = CartPage(browser, browser.current_url)
    cart.should_be_empty_cart()
    cart.should_be_empty_message()
    cart.should_be_correct_english_empty_message()

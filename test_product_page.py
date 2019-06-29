import time
import pytest
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={}"
# urls = [url.format('offer%s' % i) for i in range(10)]
urls = [url.format('newYear')]

@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.get_product_name_and_price()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_messages_about_adding()
    page.should_be_correct_product_name_and_price()


@pytest.mark.xfail(reason="need for task")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    # check with is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="need for task")
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart = CartPage(browser, browser.current_url)
    cart.should_be_empty_cart()
    cart.should_be_empty_message()
    cart.should_be_correct_english_empty_message()


@pytest.mark.login
class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        email = str(time.time()) + "@fakemail.org"
        password = 'jnWnb1548GFVW'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.get_product_name_and_price()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_messages_about_adding()
        page.should_be_correct_product_name_and_price()
        # time.sleep(30)

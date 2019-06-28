import time
import pytest
from .pages.product_page import ProductPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}"
urls = [url.format(i) for i in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.get_product_details()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_messages_about_adding()

from .base_page import BasePage
from .locators import CartPageLocators as CPL


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(
                *CPL.CART_PRODUCTS
            ), "Success products is presented, but should not be"

    def should_be_empty_message(self):
        assert self.is_element_present(
            *CPL.CART_EMPTY_MESSAGE
            ), "Not found empty message."

    def should_be_correct_english_empty_message(self):
        empty_msg = self.browser.find_element(*CPL.CART_EMPTY_MESSAGE).text
        assert 'Your basket is empty.' in empty_msg, 'Not found correct english empty basket message.'

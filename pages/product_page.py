from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    def add_product_to_cart(self):
        btn = self.browser.find_element(*PPL.ADD_TO_CART_BTN)
        btn.click()

    def get_product_name_and_price(self):
        el_name = self.browser.find_element(*PPL.PRODUCT_NAME)
        self.product_name = el_name.text
        el_price = self.browser.find_element(*PPL.PRODUCT_PRICE)
        self.product_price = el_price.text

    def should_be_messages_about_adding(self):
        err_msg = 'Not found message: {}.'.format
        assert self.is_element_present(*PPL.ADD_MSG_PRODUCT_NAME), err_msg('product added')
        assert self.is_element_present(*PPL.ADD_MSG_OFFER_TYPE), err_msg('offer type')
        assert self.is_element_present(*PPL.ADD_MSG_CART_TOTAL_PRICE), err_msg('total price')
        assert self.is_element_present(*PPL.ADD_MSG_CART_LINK), 'Not found: cart link.'
        assert self.is_element_present(*PPL.ADD_MSG_CHECKOUT_LINK), 'Not found: checkout link.'

    def should_be_correct_product_name_and_price(self):
        # check product name and price in messages
        name = self.browser.find_element(*PPL.ADD_MSG_PRODUCT_NAME).text
        assert name == self.product_name, 'Wrong name product.'
        # WARNING: price product != total price
        price_total = self.browser.find_element(*PPL.ADD_MSG_CART_TOTAL_PRICE).text
        assert price_total == self.product_price, 'Wrong price product.'

    def should_not_be_success_message_1(self):
        assert self.is_not_element_present(
                *PPL.SUCCESS_MESSAGE
            ), "Success message is presented, but should not be"

    def should_not_be_success_message_2(self):
        assert self.is_disappeared(
                *PPL.SUCCESS_MESSAGE
            ), "Success message is presented, but should not be"

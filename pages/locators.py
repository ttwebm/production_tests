from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    # messages after press add to cart button
    ADD_MSG_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')
    ADD_MSG_OFFER_TYPE = (By.CSS_SELECTOR, '.alert-success:nth-child(2) .alertinner strong')
    ADD_MSG_CART_TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    ADD_MSG_CART_LINK = (By.CSS_SELECTOR, '#messages a[href$="/basket/"]')
    ADD_MSG_CHECKOUT_LINK = (By.CSS_SELECTOR, '#messages a[href$="/checkout/"]')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert')

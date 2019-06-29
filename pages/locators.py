from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a[href$="/basket/"]')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PWD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PWD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form .btn")


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
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a[href$="/basket/"]')


class CartPageLocators:
    CART_PRODUCTS = (By.CSS_SELECTOR, '#basket_formset')
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')

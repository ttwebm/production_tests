from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.endswith('/login') or self.url.endswith('/login/'), 'url not end on "/login/"'

    def should_be_login_form(self):
        assert self.is_element_present(*LPL.LOGIN_FORM), 'Form Log In not found.'

    def should_be_register_form(self):
        assert self.is_element_present(*LPL.REGISTER_FORM), 'Form Register not found.'

    def register_new_user(self, email, password):
        el_email = self.browser.find_element(*LPL.REGISTER_EMAIL)
        el_email.send_keys(email)
        pwd1 = self.browser.find_element(*LPL.REGISTER_PWD1)
        pwd1.send_keys(password)
        pwd2 = self.browser.find_element(*LPL.REGISTER_PWD2)
        pwd2.send_keys(password)
        btn = self.browser.find_element(*LPL.REGISTER_BTN)
        btn.click()

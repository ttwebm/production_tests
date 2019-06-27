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

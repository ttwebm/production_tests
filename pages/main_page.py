from .base_page import BasePage
from .locators import MainPageLocators as MPL


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_page(self):
        link = self.browser.find_element(*MPL.BASKET_LINK)
        link.click()

import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class ButtonElement(BaseElement):
    def __init__(self, page, locator, name):
        super().__init__(page, locator, name)

    @allure.step("Check on {0}")
    def click(self):
        self.element_enabled()
        self._element.click()
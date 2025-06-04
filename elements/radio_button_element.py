import allure

from elements.base_element import BaseElement

class RadioButtonElement(BaseElement):
    def __init__(self, page, locator, name):
        super().__init__(page, locator, name)

    @allure.step("Check {0}")
    def check(self):
        self.check()
import allure
from elements.base_element import BaseElement

class InputElement(BaseElement):
    def __init__(self, page, home_page, name):
        super().__init__(page, home_page, name)

    @allure.step("Enter text in {0} input")
    def enter(self, text: str):
        self._element.fill(text)

    @allure.step("Clear {0} input")
    def clear(self):
        self._element.clear()
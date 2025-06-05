import allure

from elements.base_element import BaseElement
from pages.base_page import BasePage
from utils.locators import NavigationLocators


class NavigationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.python_button = BaseElement(page, NavigationLocators.PYTHON_BUTTON, "Python button")

    @allure.step("Go to python tutorial page")
    def open_python_tutorial_page(self):
        self.python_button.click()
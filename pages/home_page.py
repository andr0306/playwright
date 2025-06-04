from typing import List
import allure
from elements.button_element import ButtonElement
from elements.dropdown_element import DropdownElement
from elements.input_element import InputElement
from pages.base_page import BasePage
from elements.base_element import BaseElement
from utils.Locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.learn_html = ButtonElement(page, HomePageLocators.LEARN_HTML, "Learn HTML button")
        self.section = BaseElement(page, HomePageLocators.SECTION, "Section")
        self.tutorial_search_input = InputElement(page, HomePageLocators.SEARCH_TUTORIAL_INPUT, "Search input")
        self.tutorial_search_dropdown = DropdownElement(page, HomePageLocators.SEARCH_TUTORIAL_DROPDOWN, "Search tutorial dropdown")
        self.no_tutorials_found = BaseElement(page, HomePageLocators.NO_TUTORIAL_ELEMENTS, "No tutorial found")
        self._example_block = BaseElement(page, HomePageLocators.EXAMPLE_BLOCK, "Example Block")

    @allure.step("Get names of all sections")
    def get_section_names(self): return [elems.get_text() for elems in self.section.get_all()]

    @allure.step("Get all example blocks by names")
    def get_example_blocks_by_section_name(self, titles: List[str]):
        return [self._example_block.get_by_dynamic_value(title) for title in titles]

    @allure.step("Click learn HTML button")
    def click_learn_html(self):
        self.learn_html.click()

    @allure.step("Enter text into tutorial search")
    def enter_tutorial_search(self, name):
        self.tutorial_search_input.clear()
        self.tutorial_search_input.enter(name)

    @allure.step("Select tutorial option in dropdown")
    def enter_tutorial_and_select_option(self, name: str):
        self.enter_tutorial_search(name)
        self.tutorial_search_dropdown.select_option_by_name(name)

    @allure.step("Enter tutorial option and get all options")
    def enter_tutorial_and_get_all_options(self, name: str):
        self.tutorial_search_input.enter(name)
        return self.tutorial_search_dropdown.get_all_dropdown_options()
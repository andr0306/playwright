from asyncio import wait_for
from numbers import Number

import allure

from elements.button_element import ButtonElement
from pages.base_page import BasePage
from elements.base_element import BaseElement
from utils.Locators import TutorialPageLocators

class TutorialPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.tutorial_title = BaseElement(page, TutorialPageLocators.TUTORIAL_TITLE, "Tutorial page title")
        self.next_button = ButtonElement(page, TutorialPageLocators.NEXT_BUTTON, "Next button")
        self.previous_button = ButtonElement(page, TutorialPageLocators.PREVIOUS_BUTTON, "Previous button")
        self.tutorial_menu_options = BaseElement(page, TutorialPageLocators.HTML_TUTORIAL_MENU_OPTIONS, "Tutorial menu options")
        self.submit_button = ButtonElement(page, TutorialPageLocators.SUBMIT_BUTTON,"Submit button")
        self._exercise_option_by_value = ButtonElement(page, TutorialPageLocators.EXERCISE_OPTION_BY_VALUE,"Exercise option")

    @allure.step("Get tutorial side menu options")
    def get_tutorial_menu_options(self): return [elems.get_text() for elems in self.tutorial_menu_options.get_all()]

    @allure.step("Click next button and get changed title")
    def click_next_and_get_tutorial_titles(self, number: int):
        titles = []
        for title in range(number):
            titles.append(self.tutorial_title.get_text())
            self.next_button.click()
        return titles

    @allure.step("Choose an option and click submit button")
    def click_exercise_option_and_submit_form(self, value: str):
        #page load the block too long
        self.submit_button._element.wait_for(state="visible", timeout=60000)
        self._exercise_option_by_value.get_by_dynamic_value(value).click()
        self.submit_button.click()

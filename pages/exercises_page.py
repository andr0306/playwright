from elements.base_element import BaseElement
from pages.base_page import BasePage
from utils.Locators import ExercisesPageLocators


class ExercisePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.correct_answer_block = BaseElement(page, ExercisesPageLocators.CORRECT_ANSWER_BLOCK, "Correct answer block")
        self.correct_answer_message = BaseElement(page, ExercisesPageLocators.CORRECT_ANSWER_MESSAGE, "Correct answer message")
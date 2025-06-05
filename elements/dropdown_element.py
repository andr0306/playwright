import allure

from elements.base_element import BaseElement
from utils.locators import GeneralLocators

class DropdownElement(BaseElement):
    def __init__(self, page, locator, name):
        super().__init__(page, locator, name)

    @allure.step("Select option in {0}")
    def select_option_by_name(self, name: str):
        options = BaseElement(self.page, GeneralLocators.DROPDOWN_OPTION_BY_TEXT, "Dropdown options")
        option_to_select = options.get_by_dynamic_value(name)
        option_to_select.click()

    @allure.step("Get all options from {0}")
    def get_all_dropdown_options(self):
        options = BaseElement(self.page, GeneralLocators.DROPDOWN_OPTIONS, "Dropdown options").get_all()
        return [option.get_text() for option in options]




from playwright.sync_api import expect
from elements.base_element import BaseElement
import allure


class Assertions:
    @staticmethod
    @allure.step("Check {0} is visible")
    def assert_is_visible(elem: BaseElement):
        elem._element.wait_for(state="attached", timeout=6000)
        expect(elem._element).to_be_visible()

    @staticmethod
    @allure.step("Check all element from list are visible")
    def assert_all_elements_are_visible(elements: list[BaseElement]):
        for element in elements:
            Assertions.assert_is_visible(element)

    @staticmethod
    @allure.step("Check {0} is hidden")
    def assert_is_hidden(elem: BaseElement):
        expect(elem._element).to_be_hidden()

    @staticmethod
    @allure.step(f"Check {0} contain specific text")
    def assert_element_contain_text(elem: BaseElement, text: str):
        expect(elem._element).to_contain_text(text)

    @staticmethod
    @allure.step(f"Check {0} match specific text")
    def assert_text_equals(elem: BaseElement, expected_text):
        expect(elem._element).to_have_text(expected_text)

    @staticmethod
    @allure.step(f"Check {0} match specific text ignoring case")
    def assert_text_equals_ignoring_case(elem: BaseElement, expected_text):
        actual_text = elem._element.inner_text().lower()
        assert actual_text == expected_text.lower()

    @staticmethod
    @allure.step(f"Check text lists equal")
    def assert_text_lists_equal(actual_texts: list[str], expected_texts: list[str]):
        assert actual_texts == expected_texts

    @staticmethod
    @allure.step("Check text lists contain")
    def assert_text_lists_contain(actual_texts: list[str], expected_texts: list[str]):
        for i in range(len(actual_texts)):
            assert expected_texts[i] in actual_texts[i]

    @staticmethod
    @allure.step("Check text contains all values from list")
    def assert_text_contain_all_values(text: str, texts_list: list[str]):
        for t in texts_list:
            assert text in t

    @staticmethod
    @allure.step("Check text contains all values from list ignoring case")
    def assert_text_contain_all_values_ignoring_case(text: str, texts_list: list[str]):
        for t in texts_list:
            assert text.lower() in t.lower()

    @staticmethod
    @allure.step("Check element count")
    def assert_count(elements, count: int):
        assert len(elements) == count

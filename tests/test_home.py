import allure
import pytest

from utils.assertions import Assertions
import utils.constants as Constants
from utils.random import Random
from utils.data_generators import HomeTestsDataGenerator

@allure.title("Home page transitions")
def test_home_check_transitions(home_page, tutorial_page):
    Assertions.assert_is_visible(home_page.learn_html)
    home_page.learn_html.click()
    Assertions.assert_text_equals(tutorial_page.tutorial_title, Constants.Titles.HTML_TUTORIAL)
    Assertions.assert_is_hidden(home_page.learn_html)
    tutorial_page.go_to_main_page()
    Assertions.assert_is_hidden(tutorial_page.tutorial_title)
    Assertions.assert_is_visible(home_page.learn_html)

@allure.title("Home page verify sections UI")
def test_home_check_sections(home_page):
    expected_titles = ["HTML", "CSS", "JavaScript", "Python", "SQL"]
    names = home_page.get_section_names()
    Assertions.assert_text_lists_equal(names, expected_titles)
    block_elements = home_page.get_example_blocks_by_section_name(expected_titles)
    Assertions.assert_all_elements_are_visible(block_elements)

@allure.title("Home page verify search tutorial input")
@pytest.mark.parametrize("text_to_search, text_to_select, title_text", list(HomeTestsDataGenerator.verify_search_generator()))
def test_home_verify_search(home_page, tutorial_page, text_to_search, text_to_select, title_text):
    invalid_tutorial_to_search = Random.get_random_letter_string(10)
    options_found = home_page.enter_tutorial_and_get_all_options(text_to_search)
    Assertions.assert_text_contain_all_values_ignoring_case(text_to_search, options_found)
    options_found = home_page.enter_tutorial_and_get_all_options(invalid_tutorial_to_search)
    Assertions.assert_count(options_found, 1)
    Assertions.assert_is_visible(home_page.no_tutorials_found)
    home_page.enter_tutorial_and_select_option(text_to_select)
    Assertions.assert_is_visible(tutorial_page.tutorial_title)
    Assertions.assert_text_equals_ignoring_case(tutorial_page.tutorial_title, title_text)





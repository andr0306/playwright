import allure

from utils import Constants
from utils.Assertions import Assertions

@allure.description("Check tutorial titles changing")
def test_tutorial_verify_titles(home_page, tutorial_page):
    number_of_titles_to_check = 7
    home_page.click_learn_html()
    menu_titles = tutorial_page.get_tutorial_menu_options()[1:number_of_titles_to_check]
    titles = tutorial_page.click_next_and_get_tutorial_titles(number_of_titles_to_check)[1::]
    Assertions.assert_text_lists_contain( titles, menu_titles)

@allure.description("Check exercises opening")
def test_tutorial_check_exercise(navigation_page, tutorial_page, exercise_page):
    answer = "x = 5"
    navigation_page.open_python_tutorial_page()
    tutorial_page.click_exercise_option_and_submit_form(answer)


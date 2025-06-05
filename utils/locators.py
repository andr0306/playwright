class GeneralLocators:
    DROPDOWN_OPTIONS = "//a[contains(@class, 'search_item')]"
    DROPDOWN_OPTION_BY_TEXT = DROPDOWN_OPTIONS + "[span[text()='{}']]"

class NavigationLocators:
    PYTHON_BUTTON = "//div[@id='subtopnav']/a[text()='PYTHON']"

class HomePageLocators:
    LEARN_HTML = "//div[@class='w3-content']//a[text()='Learn HTML']"
    SECTION = "//div[not(contains(@class, 'pro-caption'))]/div[@class='w3-content']//div[contains(@class, 'w3-center')]//h1"
    EXAMPLE_BLOCK = "//h1[text()='{}']//parent::div/following-sibling::div"
    SEARCH_TUTORIAL_INPUT = "#search2"
    SEARCH_TUTORIAL_DROPDOWN = "#listofsearchresults"
    NO_TUTORIAL_ELEMENTS = "//a[text()='Search W3Schools']"

class TutorialPageLocators:
    TUTORIAL_TITLE = "h1.with-bookmark"
    NEXT_BUTTON = "//h1/following-sibling::div[1]/a[contains(@class, 'w3-right')]"
    PREVIOUS_BUTTON = "//h1/following-sibling::div[1]/a[contains(@class, 'w3-left')]"
    HTML_TUTORIAL_MENU_OPTIONS = "//h2[contains(text(), 'Tutorial')]/following-sibling::a"
    EXERCISE_BLOCK = "//div[@id='exercisecontainer']"
    EXERCISE_OPTION_BY_VALUE = EXERCISE_BLOCK + "//div[@class='quizoption']//code[text()='{}']"
    SUBMIT_BUTTON = EXERCISE_BLOCK + "//button"

class ExercisesPageLocators:
    CORRECT_ANSWER_BLOCK = "#xrcise-center .correctanswer"
    CORRECT_ANSWER_MESSAGE = CORRECT_ANSWER_BLOCK + " h2"
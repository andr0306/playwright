from playwright.sync_api import sync_playwright
import pytest

from pages.exercises_page import ExercisePage
from pages.home_page import HomePage
from pages.navigation_page import NavigationPage
from pages.tutorial_page import TutorialPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def home_page(page): return HomePage(page)
@pytest.fixture
def tutorial_page(page): return TutorialPage(page)
@pytest.fixture
def navigation_page(page): return NavigationPage(page)
@pytest.fixture
def exercise_page(page): return ExercisePage(page)
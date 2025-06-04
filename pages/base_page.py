import json
import os

import allure

def load_config():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(root_dir, 'config', 'config.json')

    with open(config_path, 'r') as f:
        return json.load(f)

class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = load_config()["base_url"]
        self.go_to_main_page()

    @allure.step("Go to main page")
    def go_to_main_page(self):
        self.page.goto(self.base_url)


from playwright.sync_api import Page, expect
import allure

class BaseElement:
    def __init__(self, page: Page, locator, name):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def _element(self):
        element = self.page.locator(self.locator)
        return element

    def get_all(self):
        count = self._element.count()
        return [
            BaseElement(self.page, f"{self.locator} >> nth={i}", f"{self.name} #{i}")
            for i in range(count)
        ]
    #def get_by_text(self, text, name=None):
        #return BaseElement(self.page, f"text='{text}'", name or f"Element with text '{text}'")

    def get_by_dynamic_value(self, value):
        return BaseElement(self.page, self.locator.format(value), self.name)

    @allure.step("Get text of {0}")
    def get_text(self):
        #self._element.wait_for(state="attached", timeout=5000)
        return self._element.text_content()

    @allure.step("Click on {0}")
    def click(self):
        self._element.click()

    def __repr__(self):
        return f"'{self.name}' element"
#validations
    @allure.step("Check {0} is visible")
    def element_visible(self):
        expect(self._element).to_be_visible()

    @allure.step("Check {0} is hidden")
    def element_hidden(self):
        expect(self._element).to_be_hidden()

    @allure.step("Check {0} exists")
    def element_exists(self):
        expect(self._element).to_have_count(1, timeout=5000)

    @allure.step("Check {0} is enabled")
    def element_enabled(self):
        expect(self._element).to_be_enabled()

    @allure.step("Check {0} is disabled")
    def element_disabled(self):
        expect(self._element).to_be_disabled()


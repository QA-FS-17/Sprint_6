from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Element {locator} is not visible"
        )
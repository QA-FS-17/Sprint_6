from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, description=None):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {description or locator} не стал кликабельным"
        )
        element.click()
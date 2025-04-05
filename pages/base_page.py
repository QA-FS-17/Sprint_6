from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator, element_name=""):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент '{element_name}' не стал кликабельным"
        )
        element.click()

    def get_text(self, locator, element_name=""):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент '{element_name}' не отобразился"
        )
        return element.text

    def is_element_displayed(self, locator, element_name=""):
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент '{element_name}' не найден на странице"
        )
        return element.is_displayed()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element(self, locator, timeout=10):
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент с локатором {locator}"
        )

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element
        )
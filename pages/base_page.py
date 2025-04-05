from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, locator):
        """Проверяет наличие элемента на странице без использования try-except"""
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    def wait_for_element_present(self, locator, timeout=10):
        """Явное ожидание появления элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            f"Элемент {locator} не появился за {timeout} секунд"
        )

    def wait_for_element_visible(self, locator, timeout=10):
        """Явное ожидание видимости элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            f"Элемент {locator} не стал видимым за {timeout} секунд"
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        """Явное ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            f"Элемент {locator} не стал кликабельным за {timeout} секунд"
        )
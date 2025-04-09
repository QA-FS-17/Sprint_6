# base_page.py

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Ожидание видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, tuple):
            element = self.wait_for_element(element_or_locator, timeout)
        else:
            element = element_or_locator

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.wait.until(EC.visibility_of(element))
        return element

    @allure.step("Нажать на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Прокрутить страницу до конца")
    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Закрыть текущее окно и вернуться назад")
    def close_current_window_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Проверить URL")
    def is_url_matches(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Проверить содержание URL")
    def is_url_contains(self, text):
        return text in self.driver.current_url

    @allure.step("Проверить наличие элемента")
    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    @allure.step("Клик с прокруткой")
    def click_with_scroll(self, locator, timeout=10):
        self.scroll_to_element(locator, timeout)
        self.click_on_element(locator, timeout)

    @allure.step("Получить значение атрибута элемента")
    def get_element_attribute(self, locator, attribute, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    @allure.step("Ожидание текста в элементе")
    def wait_for_text_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Получить доступ к Keys")
    def get_keys(self):
        """Возвращает класс Keys для работы с клавишами"""
        return Keys

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание содержания текста в URL")
    def wait_for_url_contains(self, text, timeout=10):
        """
        Ожидает, пока URL не будет содержать указанный текст
        """
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    @allure.step("Ожидание всех элементов")
    def wait_for_all_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
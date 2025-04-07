import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Прокрутить до выпадающего списка 'Вопросы о важном'")
    def scroll_to_pop_up_list(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажать на строку выпадающего списка")
    def click_on_string(self, string_number):
        string_locator = MainPageLocators.string_number(string_number)
        self.scroll_to_pop_up_list(string_locator)
        self.click_on_string(string_locator)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text


# main_page.py

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Прокрутить до раздела FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Ожидание загрузки раздела FAQ")
    def wait_for_faq_section(self):
        return self.wait_for_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Нажать на вопрос по индексу {index}")
    def click_question(self, index):
        question_locator = MainPageLocators.get_question_locator(index)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)
        self.wait_for_element(MainPageLocators.get_answer_locator(index))

    @allure.step("Получить текст ответа по индексу {index}")
    def get_answer_text(self, index):
        return self.get_text_on_element(MainPageLocators.get_answer_locator(index))

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)
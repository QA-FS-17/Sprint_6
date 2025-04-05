from .base_page import BasePage
from .main_page_locators import MainPageLocators


class MainPage(BasePage):
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON, "Кнопка принятия куки")

    def click_question(self, question_num):
        """Клик по вопросу в FAQ"""
        self.click(
            MainPageLocators.QUESTION_LOCATORS[question_num],
            f"Вопрос №{question_num + 1}"
        )

    def get_answer_text(self, question_num):
        """Получение текста ответа"""
        answer = self.driver.find_element(*MainPageLocators.ANSWER_LOCATORS[question_num])
        return answer.text

    def click_head_order_button(self):
        """Клик по кнопке 'Заказать' в шапке"""
        self.click(MainPageLocators.HEAD_ORDER_BUTTON, "Кнопка 'Заказать' в шапке")

    def click_foot_order_button(self):
        """Клик по кнопке 'Заказать' в футере"""
        self.click(MainPageLocators.FOOT_ORDER_BUTTON, "Кнопка 'Заказать' в футере")
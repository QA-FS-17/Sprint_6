from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def click_question(self, question_num):
        self.click(MainPageLocators.QUESTION_LOCATORS[question_num])

    def get_answer_text(self, question_num):
        return self.get_text(MainPageLocators.ANSWER_LOCATORS[question_num])

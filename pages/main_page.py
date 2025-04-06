from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.locators = MainPageLocators()

    def open(self):
        self.driver.get(self.base_url)
        self.wait.until(EC.visibility_of_element_located(self.locators.HEAD_ORDER_BUTTON))
        return self

    def click_order_button(self, button_type="HEAD"):
        locator = self.locators.HEAD_ORDER_BUTTON if button_type == "HEAD" else self.locators.FOOT_ORDER_BUTTON
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(button)
        button.click()
        return self

    def click_question(self, question_num):
        question = self.wait.until(
            EC.element_to_be_clickable(self.locators.QUESTION_LOCATORS[question_num])
        )
        self.scroll_to_element(question)
        question.click()
        return self

    def get_answer_text(self, question_num):
        return self.wait.until(
            EC.visibility_of_element_located(self.locators.ANSWER_LOCATORS[question_num])
        ).text
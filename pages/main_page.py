from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        return self

    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON, "Кнопка принятия куки")

    def click_question(self, question_num):
        self.click(
            MainPageLocators.QUESTION_LOCATORS[question_num],
            f"Вопрос №{question_num + 1}"
        )

    def get_answer_text(self, question_num):
        return self.get_text(
            MainPageLocators.ANSWER_LOCATORS[question_num],
            f"Ответ №{question_num + 1}"
        )

    def click_order_button(self, button_type):
        locator = (
            MainPageLocators.HEAD_ORDER_BUTTON if button_type == "HEAD_ORDER_BUTTON"
            else MainPageLocators.FOOT_ORDER_BUTTON
        )
        self.click(locator, f"Кнопка заказа ({button_type})")

    def is_main_page(self):
        current_url = self.driver.current_url
        return "qa-scooter.praktikum-services.ru" in current_url

    class MainPage:
        def __init__(self, driver):
            self.driver = driver

        def click(self, locator, description=None):
            """Универсальный метод для клика по элементу"""
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator),
                message=f"Элемент {description or locator} не стал кликабельным"
            )
            element.click()

        def click_question(self, question_num):
            self.click(
                MainPageLocators.QUESTION_LOCATORS[question_num],
                f"Вопрос №{question_num + 1}"
            )
from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    HEAD_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    FOOT_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    QUESTION_LOCATORS = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    ANSWER_LOCATORS = [(By.ID, f"accordion__panel-{i}") for i in range(8)]
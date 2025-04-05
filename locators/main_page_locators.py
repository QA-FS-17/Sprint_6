from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    QUESTION_LOCATORS = [(By.ID, f"accordion__heading-{i}") for i in range(8)]
    ANSWER_LOCATORS = [(By.ID, f"accordion__panel-{i}") for i in range(8)]
    HEAD_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[contains(@class, 'Header')]]")
    FOOT_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать') and ancestor::div[contains(@class, 'Home_FinishButton')]]")
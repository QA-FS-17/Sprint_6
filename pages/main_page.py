from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    FOOTER_ORDER_BUTTON = (
    By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def click_header_order_button(self):
        self.click_element(self.HEADER_ORDER_BUTTON)

    def click_footer_order_button(self):
        self.click_element(self.FOOTER_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)
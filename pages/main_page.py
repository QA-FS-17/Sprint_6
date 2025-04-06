from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    HEADER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    FOOTER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")

    def click_header_order_button(self):
        self.click_element(self.HEADER_ORDER_BUTTON)

    def click_footer_order_button(self):
        self.find_element(self.FOOTER_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.find_element(self.FOOTER_ORDER_BUTTON))
        self.click_element(self.FOOTER_ORDER_BUTTON)

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    def click_samokat_logo(self):
        self.click_element(self.SAMOKAT_LOGO)
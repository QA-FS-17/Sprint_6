from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderModal(BasePage):
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SUCCESS_MODAL_TEXT = (By.XPATH, "//div[contains(@class, 'Order_Text')]")

    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    def is_success_modal_displayed(self):
        return self.find_element(self.SUCCESS_MODAL).is_displayed()

    def get_success_modal_text(self):
        return self.find_element(self.SUCCESS_MODAL_TEXT).text
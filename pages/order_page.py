from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    def fill_order_form(self, order_data):
        self._input_text(self.locators.NAME_INPUT, order_data['name'])
        self._input_text(self.locators.LASTNAME_INPUT, order_data['lastname'])
        self._input_text(self.locators.ADDRESS_INPUT, order_data['address'])
        self._select_metro_station(order_data['metro'])
        self._input_phone(order_data['phone'])
        self._click(self.locators.NEXT_BUTTON)
        return self

    def fill_rental_details(self, order_data):
        self._input_date(order_data['date'])
        self._select_rental_period(order_data['rental_period'])
        self._select_color(order_data['color'])
        if order_data.get('comment'):
            self._input_text(self.locators.COMMENT_INPUT, order_data['comment'])
        return self

    def confirm_order(self):
        self._click(self.locators.ORDER_BUTTON)
        self._click(self.locators.CONFIRM_BUTTON)
        return self

    def is_success_message_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.locators.SUCCESS_MESSAGE)
        ).is_displayed()

    def _select_metro_station(self, station_name):
        self._click(self.locators.METRO_INPUT)
        search_input = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'select-search__input'))
        )
        search_input.send_keys(station_name[:3])
        station = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'select-search__option') and contains(., '{station_name}')]")
            )
        )
        station.click()

    def _select_rental_period(self, period):
        self._click(self.locators.RENTAL_PERIOD)
        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and contains(., '{period}')]")
            )
        )
        option.click()

    def _select_color(self, color):
        locator = self.locators.COLOR_BLACK if color == 'black' else self.locators.COLOR_GREY
        self._click(locator)

    def _input_date(self, date):
        self._input_text(self.locators.DATE_INPUT, date)

    def _input_phone(self, phone):
        self._input_text(self.locators.PHONE_INPUT, phone)

    def _input_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def _click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()
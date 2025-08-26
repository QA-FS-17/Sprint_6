# order_page.py

import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_order_button_top(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_order_button_bottom(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Заполнить персональную информацию')
    def fill_personal_info(self, name, lastname, address, metro, phone):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro)
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные аренды')
    def fill_rental_details(self, date, period, color, comment):
        date_input = self.wait_for_element(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        self.close_date_picker()

        self.select_rental_period(period)
        self.select_color(color)
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)

    def close_date_picker(self):
        date_input = self.wait_for_element(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(self.get_keys().ESCAPE)

        if self.is_element_present(OrderPageLocators.DATE_PICKER):
            self.click_on_element(OrderPageLocators.BODY)
            if self.is_element_present(OrderPageLocators.DATE_PICKER):
                raise Exception("Не удалось закрыть календарь даты")

    def select_metro_station(self, metro_name):
        self.accept_cookies()
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.wait_for_element(OrderPageLocators.METRO_DROPDOWN)

        stations = self.wait_for_all_elements(OrderPageLocators.METRO_OPTION)
        for station in stations:
            if metro_name in station.text:
                self.scroll_to_element(station)
                station.click()
                return

        raise ValueError(f"Станция '{metro_name}' не найдена")

    def accept_cookies(self):
        if self.is_element_present(OrderPageLocators.COOKIE_BANNER):
            self.click_on_element(OrderPageLocators.COOKIE_ACCEPT_BUTTON)
            self.wait_for_element_to_disappear(OrderPageLocators.COOKIE_BANNER)

    def select_rental_period(self, period):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (
            OrderPageLocators.RENTAL_OPTION[0],
            OrderPageLocators.RENTAL_OPTION[1].format(period)
        )
        self.click_on_element(period_locator)

    def select_color(self, color):
        color_locator = OrderPageLocators.COLOR_BLACK if color == "black" else OrderPageLocators.COLOR_GREY
        self.click_on_element(color_locator)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.FINAL_ORDER_BUTTON)
        self.wait_for_element(OrderPageLocators.CONFIRM_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    def is_order_successful(self):
        """Проверяет успешность заказа по наличию модального окна"""
        return self.is_element_present(OrderPageLocators.ORDER_SUCCESS_MODAL)

    def get_success_message(self):
        """Возвращает текст сообщения об успешном заказе"""
        return self.wait_for_element(OrderPageLocators.ORDER_SUCCESS_MODAL).text
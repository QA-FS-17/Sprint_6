from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_personal_info(self, name, last_name, address, phone, metro_station):
        """Заполняет персональные данные с использованием методов BasePage"""
        self.wait_for_element_visible(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.wait_for_element_visible(OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.wait_for_element_visible(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.wait_for_element_visible(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.select_metro_station(metro_station)
        return self

    def select_metro_station(self, station_name):
        """Выбирает станцию метро с явными ожиданиями"""
        self.wait_for_element_clickable(OrderPageLocators.METRO_INPUT).click()
        station_locator = (OrderPageLocators.METRO_OPTION[0],
                         OrderPageLocators.METRO_OPTION[1].format(station_name))
        self.wait_for_element_clickable(station_locator).click()
        return self

    def go_to_rental_info(self):
        """Переходит к данным аренды"""
        self.wait_for_element_clickable(OrderPageLocators.NEXT_BUTTON).click()
        return self

    def fill_rental_info(self, date, period, color, comment=None):
        """Заполняет данные аренды"""
        self.wait_for_element_visible(OrderPageLocators.DELIVERY_DATE).send_keys(date)
        self.select_rental_period(period)
        self.select_scooter_color(color)
        if comment:
            self.wait_for_element_visible(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        return self

    def select_rental_period(self, period):
        """Выбирает срок аренды"""
        self.wait_for_element_clickable(OrderPageLocators.RENTAL_PERIOD).click()
        period_locator = (OrderPageLocators.RENTAL_OPTION[0],
                        OrderPageLocators.RENTAL_OPTION[1].format(period))
        self.wait_for_element_clickable(period_locator).click()
        return self

    def select_scooter_color(self, color):
        """Выбирает цвет самоката"""
        locator = OrderPageLocators.COLOR_BLACK if color == "black" else OrderPageLocators.COLOR_GREY
        self.wait_for_element_clickable(locator).click()
        return self

    def submit_order(self):
        """Отправляет заказ"""
        self.wait_for_element_clickable(OrderPageLocators.ORDER_BUTTON).click()
        return self

    def confirm_order(self):
        """Подтверждает заказ"""
        self.wait_for_element_clickable(OrderPageLocators.CONFIRM_BUTTON).click()
        return self

    def is_order_confirmed(self):
        """Проверяет подтверждение заказа"""
        return self.is_element_present(OrderPageLocators.SUCCESS_MESSAGE)
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_order_form(self, order_data):
        self._fill_personal_data(order_data)
        self._click_next_button()
        self._fill_rental_data(order_data)

    def confirm_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON, "Кнопка 'Заказать'")
        self.click(OrderPageLocators.CONFIRM_BUTTON, "Кнопка подтверждения заказа")

    def is_success_message_displayed(self):
        return self.is_element_displayed(
            OrderPageLocators.SUCCESS_MESSAGE,
            "Сообщение об успешном оформлении"
        )

    def click_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO, "Логотип Самоката")

    # Приватные вспомогательные методы
    def _fill_personal_data(self, data):
        self._input_text(OrderPageLocators.NAME_INPUT, data["name"], "Имя")
        self._input_text(OrderPageLocators.LAST_NAME_INPUT, data["surname"], "Фамилия")
        self._input_text(OrderPageLocators.ADDRESS_INPUT, data["address"], "Адрес")
        self._input_text(OrderPageLocators.PHONE_INPUT, data["phone"], "Телефон")
        self._select_metro(data["metro"])

    def _fill_rental_data(self, data):
        self._input_text(OrderPageLocators.DELIVERY_DATE, data["delivery_date"], "Дата доставки")
        self._select_rental_period(data["rental_period"])
        if data.get("color"):
            self._select_color(data["color"])
        if data.get("comment"):
            self._input_text(OrderPageLocators.COMMENT_INPUT, data["comment"], "Комментарий")

    def _click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON, "Кнопка 'Далее'")

    def _input_text(self, locator, text, field_name):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Поле '{field_name}' не найдено"
        )
        element.clear()
        element.send_keys(text)

    def _select_metro(self, station_name):
        self.click(OrderPageLocators.METRO_INPUT, "Поле выбора метро")
        station_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(station_name)
        )
        self.click(station_locator, f"Станция метро '{station_name}'")

    def _select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD, "Поле 'Срок аренды'")
        period_locator = (
            OrderPageLocators.RENTAL_OPTION[0],
            OrderPageLocators.RENTAL_OPTION[1].format(period)
        )
        self.click(period_locator, f"Период аренды '{period}'")

    def _select_color(self, color):
        color_locator = getattr(OrderPageLocators, f"COLOR_{color.upper()}")
        self.click(color_locator, f"Цвет '{color}'")
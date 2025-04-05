from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from ..locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_order_form(self, order_data):
        """
        Полное заполнение формы заказа
        При ошибке тест упадёт с явным сообщением
        """
        self._fill_personal_data(order_data)
        self._click_next_button()
        self._fill_rental_data(order_data)

    def _fill_personal_data(self, data):
        """Заполнение раздела с персональными данными"""
        self._input_text_safe(OrderPageLocators.NAME_FIELD, data["name"], "Поле 'Имя'")
        self._input_text_safe(OrderPageLocators.SURNAME_FIELD, data["surname"], "Поле 'Фамилия'")
        self._input_text_safe(OrderPageLocators.ADDRESS_FIELD, data["address"], "Поле 'Адрес'")
        self._input_text_safe(OrderPageLocators.PHONE_FIELD, data["phone"], "Поле 'Телефон'")
        self._select_metro_station_safe(data["metro"])

    def _fill_rental_data(self, data):
        """Заполнение раздела с данными аренды"""
        self._input_text_safe(OrderPageLocators.DATE_FIELD, data["delivery_date"], "Поле 'Дата доставки'")
        self._select_rental_period_safe(data["rental_period"])

        if "color" in data:
            self._select_color_safe(data["color"])

        if "comment" in data:
            self._input_text_safe(OrderPageLocators.COMMENT_FIELD, data["comment"], "Поле 'Комментарий'")

    def _input_text_safe(self, locator, text, field_name=""):
        """
        Безопасный ввод текста с явными проверками
        :param field_name: Название поля для сообщения об ошибке
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator),
            message=f"{field_name} не найдено или не видимо"
        )
        element.clear()
        element.send_keys(text)

    def _select_metro_station_safe(self, station_name):
        """Выбор станции метро с явными проверками"""
        self._click_safe(OrderPageLocators.METRO_FIELD, "Поле выбора метро")

        station_locator = (
            OrderPageLocators.METRO_STATION[0],
            OrderPageLocators.METRO_STATION[1].format(station_name)
        )
        self._click_safe(station_locator, f"Станция метро '{station_name}'")

    def _select_rental_period_safe(self, period):
        """Выбор срока аренды с явными проверками"""
        self._click_safe(OrderPageLocators.RENTAL_PERIOD_DROPDOWN, "Выпадающий список 'Срок аренды'")

        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period)
        )
        self._click_safe(period_locator, f"Период аренды '{period}'")

    def _select_color_safe(self, color):
        """Выбор цвета самоката с явными проверками"""
        color_locator = (
            OrderPageLocators.COLOR_CHECKBOX[0],
            OrderPageLocators.COLOR_CHECKBOX[1].format(color)
        )
        self._click_safe(color_locator, f"Чекбокс цвета '{color}'")

    def _click_next_button(self):
        """Клик по кнопке 'Далее' с проверкой"""
        self._click_safe(OrderPageLocators.NEXT_BUTTON, "Кнопка 'Далее'")

    def _click_safe(self, locator, element_name=""):
        """
        Безопасный клик с явными проверками
        :param element_name: Название элемента для сообщения об ошибке
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {element_name} не кликабелен"
        ).click()

    def confirm_order(self):
        """Подтверждение заказа с проверками"""
        self._click_safe(OrderPageLocators.ORDER_BUTTON, "Кнопка 'Заказать'")
        self._click_safe(OrderPageLocators.CONFIRM_BUTTON, "Кнопка подтверждения 'Да'")

    def is_success_message_displayed(self):
        """Проверка отображения сообщения об успехе"""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE),
            message="Сообщение об успешном оформлении не отобразилось"
        )
        return element.is_displayed()

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self._click_safe(OrderPageLocators.SCOOTER_LOGO, "Логотип Самоката")

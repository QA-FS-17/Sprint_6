import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_order_button_top(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_order_button_bottom(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Заполнить персональную информацию: {name} {lastname}')
    def fill_personal_info(self, name, lastname, address, metro, phone):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)

        self.send_keys_to_input(OrderPageLocators.METRO_STATION_INPUT, metro)
        metro_option = (OrderPageLocators.METRO_OPTION[0],
                        OrderPageLocators.METRO_OPTION[1].format(metro))
        self.click_on_element(metro_option)

        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные аренды: срок {period}, цвет {color}')
    def fill_rental_details(self, date, period, color, comment):
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)
        self.wait_for_element_to_disappear(OrderPageLocators.DATE_PICKER)

        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        rental_option = (OrderPageLocators.RENTAL_OPTION[0],
                         OrderPageLocators.RENTAL_OPTION[1].format(period))
        self.click_on_element(rental_option)

        color_locator = OrderPageLocators.COLOR_BLACK if color == "black" else OrderPageLocators.COLOR_GREY
        self.click_on_element(color_locator)

        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)
        self.click_on_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получить сообщение об успешном заказе')
    def get_success_message(self):
        return self.get_text_on_element(OrderPageLocators.SUCCESS_MESSAGE)
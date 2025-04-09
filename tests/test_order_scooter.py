import allure
import pytest
from data import TestData

@allure.feature('Тесты заказа самоката')
class TestOrderScooter:
    @allure.title('Заказ через верхнюю кнопку')
    def test_order_via_top_button(self, order_page, order_data):
        with allure.step('1. Нажать верхнюю кнопку "Заказать"'):
            order_page.click_order_button_top()

        self._complete_order_flow(order_page, order_data)

    @allure.title('Заказ через нижнюю кнопку')
    def test_order_via_bottom_button(self, order_page, order_data):
        with allure.step('1. Прокрутить и нажать нижнюю кнопку "Заказать"'):
            order_page.scroll_to_bottom()
            order_page.click_order_button_bottom()

        self._complete_order_flow(order_page, order_data)

    def _complete_order_flow(self, order_page, order_data):
        with allure.step('2. Заполнить персональные данные'):
            order_page.fill_personal_info(
                name=order_data['name'],
                lastname=order_data['lastname'],
                address=order_data['address'],
                metro=order_data['metro'],
                phone=order_data['phone']
            )

        with allure.step('3. Заполнить данные аренды'):
            order_page.fill_rental_details(
                date=order_data['date'],
                period=order_data['rental_period'],
                color=order_data['color'],
                comment=order_data['comment']
            )

        with allure.step('4. Подтвердить заказ'):
            order_page.confirm_order()

        with allure.step('5. Проверить успешное оформление'):
            assert "Заказ оформлен" in order_page.get_success_message()

@allure.feature('Тесты логотипов')
class TestLogos:
    @allure.title('Проверка логотипа Самоката')
    def test_scooter_logo_redirect(self, main_page):
        with allure.step('1. Нажать логотип Самоката'):
            main_page.click_scooter_logo()

        with allure.step('2. Проверить переход на главную'):
            assert main_page.is_url_matches("https://qa-scooter.praktikum-services.ru/")

    @allure.title('Проверка логотипа Яндекса')
    def test_yandex_logo_redirect(self, main_page):
        with allure.step('1. Нажать логотип Яндекса'):
            main_page.click_yandex_logo()

        with allure.step('2. Проверить открытие Дзена'):
            main_page.switch_to_new_window()
            assert main_page.is_url_contains("dzen.ru")
            main_page.close_current_window_and_switch_back()

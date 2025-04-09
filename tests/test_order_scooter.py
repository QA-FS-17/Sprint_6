# tests\test_order_scooter.py

import allure
from .order_helpers import complete_order_flow  # Импорт общего метода


@allure.feature('Тесты заказа самоката')
class TestOrderScooter:
    @allure.title('Заказ через верхнюю кнопку')
    def test_order_via_top_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через верхнюю кнопку
        """
        with allure.step('1. Нажать верхнюю кнопку "Заказать"'):
            order_page.click_order_button_top()

        complete_order_flow(order_page, order_data)  # Используем импортированный метод

    @allure.title('Заказ через нижнюю кнопку')
    def test_order_via_bottom_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через нижнюю кнопку
        """
        with allure.step('1. Нажать нижнюю кнопку "Заказать"'):
            order_page.click_order_button_bottom()

        complete_order_flow(order_page, order_data)  # Используем импортированный метод


@allure.feature('Тесты логотипов')
class TestLogos:
    @allure.title('Проверка логотипа Самоката')
    def test_scooter_logo_redirect(self, main_page):
        """
        Тест проверяет переход на главную страницу при клике на логотип Самоката
        """
        with allure.step('1. Нажать логотип Самоката'):
            main_page.click_scooter_logo()

        with allure.step('2. Проверить переход на главную'):
            expected_url = "https://qa-scooter.praktikum-services.ru/"
            current_url = main_page.get_current_url()
            assert current_url == expected_url, \
                f"Ожидался URL: {expected_url}, получен: {current_url}"

    @allure.title('Проверка логотипа Яндекса')
    def test_yandex_logo_redirect(self, main_page):
        """
        Тест проверяет переход на Дзен при клике на логотип Яндекса
        """
        with allure.step('1. Нажать логотип Яндекса'):
            main_page.click_yandex_logo()

        with allure.step('2. Проверить открытие Дзена'):
            main_page.switch_to_new_window()
            main_page.wait_for_url_contains("dzen.ru", timeout=15)
            current_url = main_page.get_current_url().lower()
            assert "dzen.ru" in current_url, \
                f"URL должен содержать 'dzen.ru', текущий URL: {current_url}"
            main_page.close_current_window_and_switch_back()
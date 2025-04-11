# test_order_scooter.py

import allure
from helpers.order_helpers import complete_order_flow


@allure.feature('Тесты заказа самоката')
class TestOrderScooter:
    @allure.title('Заказ через верхнюю кнопку')
    def test_order_via_top_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через верхнюю кнопку
        """
        with allure.step('1. Нажать верхнюю кнопку "Заказать"'):
            order_page.click_order_button_top()

        complete_order_flow(order_page, order_data)

        with allure.step('Проверить успешное оформление заказа'):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title('Заказ через нижнюю кнопку')
    def test_order_via_bottom_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через нижнюю кнопку
        """
        with allure.step('1. Нажать нижнюю кнопку "Заказать"'):
            order_page.click_order_button_bottom()

        complete_order_flow(order_page, order_data)

        with allure.step('Проверить успешное оформление заказа'):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"


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
            assert main_page.get_current_url() == expected_url

    @allure.feature('Тесты логотипов')
    class TestLogos:
        @allure.title('Проверка логотипа Яндекса')
        def test_yandex_logo_redirect(self, main_page, request):
            """
            Тест проверяет переход на Дзен при клике на логотип Яндекса
            """
            request.node.window_opened = True  # Помечаем тест для финализатора

            with allure.step('1. Нажать логотип Яндекса'):
                main_page.click_yandex_logo()

            with allure.step('2. Проверить открытие Дзена'):
                main_page.switch_to_new_window()
                main_page.wait_for_url_contains("dzen.ru", timeout=15)
                assert "dzen.ru" in main_page.get_current_url().lower()
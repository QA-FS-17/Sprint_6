# test_order_scooter.py

import allure


@allure.feature('Тесты заказа самоката')
class TestOrderScooter:
    @allure.title('Заказ через верхнюю кнопку')
    def test_order_via_top_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через верхнюю кнопку
        """
        with allure.step('1. Нажать верхнюю кнопку "Заказать"'):
            order_page.click_order_button_top()

        self._complete_order_flow(order_page, order_data)

    @allure.title('Заказ через нижнюю кнопку')
    def test_order_via_bottom_button(self, order_page, order_data):
        """
        Тест проверяет полный процесс оформления заказа через нижнюю кнопку
        """
        with allure.step('1. Нажать нижнюю кнопку "Заказать"'):
            order_page.click_order_button_bottom()

        self._complete_order_flow(order_page, order_data)

    def _complete_order_flow(self, order_page, order_data):
        """
        Общий метод для выполнения полного потока заказа
        """
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
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Ожидалось сообщение 'Заказ оформлен', получено: '{success_message}'"


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
            # Переключаемся на новое окно
            main_page.switch_to_new_window()

            # Явное ожидание загрузки страницы
            main_page.wait_for_url_contains("dzen.ru", timeout=15)

            # Проверяем URL
            current_url = main_page.get_current_url().lower()
            assert "dzen.ru" in current_url, \
                f"URL должен содержать 'dzen.ru', текущий URL: {current_url}"

            # Закрываем окно и возвращаемся назад
            main_page.close_current_window_and_switch_back()
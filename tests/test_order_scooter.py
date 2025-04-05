import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.generate_data import generate_order_data


@allure.suite("Тесты оформления заказа")
class TestOrderScooter:
    @allure.title("Оформление заказа через {button_name} кнопку")
    @allure.description("""
    Проверка полного цикла оформления заказа самоката.
    Шаги:
    1. Открываем главную страницу
    2. Нажимаем кнопку 'Заказать' ({button_name})
    3. Заполняем форму заказа тестовыми данными
    4. Подтверждаем заказ
    5. Проверяем сообщение об успешном оформлении
    6. Возвращаемся на главную страницу через логотип
    """)
    @pytest.mark.parametrize("order_button_locator, order_data, button_name", [
        ("HEAD_ORDER_BUTTON", generate_order_data(), "верхнюю"),
        ("FOOT_ORDER_BUTTON", generate_order_data(), "нижнюю"),
    ], ids=["Заказ через верхнюю кнопку", "Заказ через нижнюю кнопку"])
    def test_order_scooter(self, driver, order_button_locator, order_data, button_name):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step(f"Нажимаем {button_name} кнопку 'Заказать'"):
            main_page.click_order_button(order_button_locator)

        with allure.step("Заполняем форму заказа"):
            order_page.fill_order_form(order_data)

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()

        with allure.step("Проверяем сообщение об успешном оформлении"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном оформлении не отображается"

        with allure.step("Возвращаемся на главную страницу через логотип"):
            order_page.click_scooter_logo()

        with allure.step("Проверяем, что вернулись на главную страницу"):
            assert main_page.is_main_page(), "Не удалось вернуться на главную страницу"
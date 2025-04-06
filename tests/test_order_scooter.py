import allure
import pytest
from utils.generate_data import generate_order_data


@allure.feature("Оформление заказа")
class TestOrderScooter:
    @allure.title("Оформление заказа через {button_type} кнопку")
    @pytest.mark.parametrize("button_type", ["HEAD", "FOOT"])
    def test_order_scooter(self, main_page, order_page, button_type):
        order_data = generate_order_data()

        with allure.step(f"1. Нажать кнопку 'Заказать' ({button_type})"):
            main_page.click_order_button(button_type)

        with allure.step("2. Заполнить форму заказа"):
            order_page.fill_order_form(order_data)
            order_page.fill_rental_details(order_data)

        with allure.step("3. Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("4. Проверить сообщение об успехе"):
            assert order_page.is_success_message_displayed()
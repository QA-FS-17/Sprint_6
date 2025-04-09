# tests\order_helpers.py

import allure

def complete_order_flow(order_page, order_data):
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

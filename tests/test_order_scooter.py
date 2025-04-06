import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.generate_data import generate_order_data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('Order Flow')
class TestOrderFlow:
    @allure.title('Order from {entry_point}')
    @pytest.mark.parametrize('entry_point', ['head', 'foot'])
    def test_successful_order_flow(self, driver, entry_point):
        order_data = generate_order_data()
        allure.attach(str(order_data), name="Test Data", attachment_type=allure.attachment_type.TEXT)

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Main page steps
        main_page.open()
        main_page.accept_cookies()

        # Start order
        if entry_point == 'head':
            main_page.click_head_order_button()
        else:
            main_page.scroll_and_click_foot_order_button()

        # Fill forms
        order_page.fill_personal_info(
            order_data['name'],
            order_data['lastname'],
            order_data['address'],
            order_data['metro'],
            order_data['phone']
        )

        order_page.fill_rental_details(
            order_data['date'],
            order_data['rental_period'],
            order_data['color'],
            order_data.get('comment', '')
        )

        # Verify successful order
        assert "Заказ оформлен" in order_page.confirm_and_verify_order()


@allure.feature('Navigation')
class TestNavigation:
    @allure.title('Test {logo} logo')
    @pytest.mark.parametrize('logo', ['scooter', 'yandex'])
    def test_logo_navigation(self, driver, logo):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        if logo == 'scooter':
            main_page.click_scooter_logo()
            assert main_page.is_on_main_page()
        else:
            main_page.click_yandex_logo()
            main_page.switch_to_new_window()
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
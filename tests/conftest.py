import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.generate_data import generate_order_data

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def accept_cookies(main_page):
    main_page.accept_cookies()
    return main_page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def fill_order_form_first_page(driver, accept_cookies):
    order_data = generate_order_data()
    page = OrderPage(driver)
    (page.fill_personal_info(
        order_data["name"],
        order_data["surname"],
        order_data["address"],
        order_data["phone"],
        order_data["metro"]
     ).go_to_rental_info())
    return order_data, page

@pytest.fixture
def complete_scooter_order(fill_order_form_first_page):
    order_data, page = fill_order_form_first_page
    (page.fill_rental_info(
        "2024-12-31",
        "сутки",
        "grey",
        "Тестовый заказ"
     ).submit_order()
     .confirm_order())
    return order_data, page
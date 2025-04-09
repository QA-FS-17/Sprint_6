# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.order_page import OrderPage
from pages.main_page import MainPage
from utils.generate_data import generate_order_data
from config import Urls


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get(Urls.MAIN)
    yield driver
    driver.quit()

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_data():
    return generate_order_data()
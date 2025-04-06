import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)
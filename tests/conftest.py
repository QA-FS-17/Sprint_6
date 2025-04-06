import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    # Инициализация драйвера
    driver = webdriver.Firefox(options=options)

    # Установка оптимального размера окна
    driver.maximize_window()  # Максимизирует окно с учетом границ экрана

    yield driver
    driver.quit()
# Базовые фикстуры

# Фикстура драйвера(основная)
# Открывает и закрывает браузер для каждого теста

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    # Настройки Firefox
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Путь к Firefox
    options.add_argument("--width=1920")  # Ширина окна
    options.add_argument("--height=1080")  # Высота окна
    # Инициализация драйвера
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver  # Передаем драйвер в тест
    # Закрытие браузера после теста
    driver.quit()

# Фикстура для принятия куки
# Автоматически закрывает куки-баннер

from pages.main_page import MainPage


@pytest.fixture(scope="function")
def accept_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()  # Метод в MainPage, который кликает на кнопку "Да" для куки

# Фикстуры для тестов заказа

# Фикстура заполнения формы заказа
# Подготавливает данные и заполняет первую страницу формы

from utils.generate_data import generate_order_data
from pages.order_page import OrderPage


@pytest.fixture
def fill_order_form_first_page(driver):
    order_data = generate_order_data()  # Генерация тестовых данных

    order_page = OrderPage(driver)
    order_page.fill_name(order_data["name"])
    order_page.fill_last_name(order_data["surname"])
    order_page.fill_address(order_data["address"])
    order_page.fill_phone(order_data["phone"])
    order_page.click_next_button()

    return order_data  # Можно использовать в тесте

# Фикстура для успешного заказа
# Полностью проходит весь флоу заказа

@pytest.fixture
def complete_scooter_order(driver, fill_order_form_first_page):
    order_page = OrderPage(driver)
    order_data = fill_order_form_first_page

    # Заполнение второй страницы
    order_page.set_delivery_date("2024-12-31")
    order_page.select_rental_period("сутки")  # Выбираем из выпадающего списка
    order_page.select_color("grey")  # Выбираем цвет
    order_page.add_comment("Тестовый заказ")
    order_page.confirm_order()

    return order_data

# Фикстура для Allure - отчетов
# Добавляет скриншоты при падении теста

import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]  # Получаем драйвер из теста
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )


# Фикстура для параметризованных тестов
# Пример, для тестов с разными точками входа(верхняя / нижняя кнопка заказа)

@pytest.fixture(params=["HEAD_ORDER_BUTTON", "FOOT_ORDER_BUTTON"])
def order_button_locator(request):
    return request.param  # Возвращает название локатора для кнопки

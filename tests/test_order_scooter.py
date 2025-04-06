import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.success_page import OrderModal
import allure


@pytest.mark.parametrize(
    "order_button_locator, order_data",
    [
        ("header", {
            "name": "Иван",
            "last_name": "Иванов",
            "address": "Москва, ул. Тверская, 1",
            "metro_station": "Тверская",
            "phone": "+79998887766",
            "delivery_date": "01.01.2025",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвонить за час"
        }),
        ("footer", {
            "name": "Петр",
            "last_name": "Петров",
            "address": "Санкт-Петербург, Невский пр., 10",
            "metro_station": "Невский проспект",
            "phone": "+79997776655",
            "delivery_date": "15.01.2025",
            "rental_period": "двое суток",
            "color": "grey",
            "comment": ""
        })
    ]
)
@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий заказа")
def test_order_flow(driver, order_button_locator, order_data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    order_modal = OrderModal(driver)

    with allure.step("Открыть главную страницу"):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.accept_cookies()

    with allure.step(f"Нажать кнопку 'Заказать' в {'хэдере' if order_button_locator == 'header' else 'футере'}"):
        if order_button_locator == "header":
            main_page.click_header_order_button()
        else:
            main_page.click_footer_order_button()

    with allure.step("Заполнить первую страницу формы заказа"):
        order_page.fill_first_page(
            order_data["name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )

    with allure.step("Заполнить вторую страницу формы заказа"):
        order_page.fill_second_page(
            order_data["delivery_date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )

    with allure.step("Подтвердить заказ"):
        order_modal.confirm_order()

    with allure.step("Проверить успешное оформление заказа"):
        assert order_modal.is_success_modal_displayed(), "Модальное окно успешного заказа не отображается"
        assert "Заказ оформлен" in order_modal.get_success_modal_text(), "Текст успешного заказа не соответствует ожидаемому"


@allure.feature("Проверка логотипов")
def test_logos(driver):
    main_page = MainPage(driver)

    with allure.step("Открыть главную страницу"):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.accept_cookies()

    with allure.step("Проверить логотип Самоката"):
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Логотип Самоката не ведет на главную страницу"

    with allure.step("Проверить логотип Яндекса"):
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url, "Логотип Яндекса не ведет на Дзен"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
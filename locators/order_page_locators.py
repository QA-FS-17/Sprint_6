# locators\order_page_locators.py

from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH,
                        "//button[contains(@class, 'Button_Button__ra12g') and not(contains(@class, 'Button_Middle')) and contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (
    By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")

    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.CLASS_NAME, "select-search__select")
    METRO_OPTION = (By.CLASS_NAME, "select-search__option")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")

    # Модальное окно
    CONFIRM_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Дополнительные элементы
    BODY = (By.TAG_NAME, "body")

    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")

from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""

    # Кнопки вызова формы заказа (главная страница)
    ORDER_BUTTON_TOP = (By.XPATH,
                        "//button[contains(@class, 'Button_Button__ra12g') and not(contains(@class, 'Button_Middle')) and contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (
    By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")

    # Первая страница формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница формы
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # Модальное окно
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Дополнительные элементы
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker")
    METRO_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__option') and text()='{}']")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
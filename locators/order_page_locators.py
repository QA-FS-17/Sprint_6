from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""

    # ===== Локаторы первой страницы формы =====
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Локатор поля метро + вариант выбора станции
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__option')]")

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # ===== Локаторы второй страницы формы =====
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_INPUT_LABEL = (By.XPATH, "//label[contains(text(), 'Когда привезти самокат')]")

    # Локаторы для выбора срока аренды
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")

    # Локаторы цветов
    COLOR_BLACK = (By.ID, "black")  # Чёрный самокат
    COLOR_GREY = (By.ID, "grey")  # Серый самокат

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')

    # ===== Кнопки заказа на главной =====
    ORDER_BUTTON_TOP = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g']"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']"
    )

    # ===== Локаторы модального окна =====
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Дополнительные локаторы для календаря
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker")
    DATE_PICKER_DAY = (By.CLASS_NAME, "react-datepicker__day--selected")
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (
    By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
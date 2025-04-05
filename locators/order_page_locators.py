from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Персональные данные
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_OPTION = (By.XPATH, '//div[text()="{}"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Данные аренды
    DELIVERY_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_OPTION = (By.XPATH, '//div[text()="{}"]')
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Подтверждение заказа
    ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(text(), "Заказ оформлен")]')

    # Навигация
    SCOOTER_LOGO = (By.XPATH, '//a[@href="/"]')
from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    # Локаторы для первой страницы формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_ITEM = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы формы заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOX = (By.XPATH, "//input[@type='checkbox']/..")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.input_text(self.NAME_INPUT, name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.ADDRESS_INPUT, address)
        self.input_text(self.METRO_STATION_INPUT, metro_station)
        self.click_element(self.METRO_STATION_ITEM)
        self.input_text(self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_page(self, delivery_date, rental_period, color, comment):
        self.input_text(self.DELIVERY_DATE_INPUT, delivery_date)
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        rental_period_option = (
        self.RENTAL_PERIOD_OPTION[0], f"//div[@class='Dropdown-option'][text()='{rental_period}']")
        self.click_element(rental_period_option)

        if color:
            color_locator = (self.COLOR_CHECKBOX[0], f"//input[@id='{color}']/..")
            self.click_element(color_locator)

        if comment:
            self.input_text(self.COMMENT_INPUT, comment)

        self.click_element(self.ORDER_BUTTON)
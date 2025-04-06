from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//button")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Second form
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOX = (By.XPATH, "//input[@class='Checkbox_Input__14A2w']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    def fill_first_form(self, name, last_name, address, metro_station, phone):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        self.find_element(self.METRO_INPUT).click()
        metro_station_locator = (By.XPATH, f"//button/div[text()='{metro_station}']")
        self.click_element(metro_station_locator)
        self.find_element(self.PHONE_INPUT).send_keys(phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        self.find_element(self.DATE_INPUT).send_keys(date)
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)
        rental_period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']")
        self.click_element(rental_period_locator)

        if color.lower() == 'black':
            self.click_element((By.ID, "black"))
        elif color.lower() == 'grey':
            self.click_element((By.ID, "grey"))

        self.find_element(self.COMMENT_INPUT).send_keys(comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_ORDER_BUTTON)
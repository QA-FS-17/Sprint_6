from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_personal_info(self, name, lastname, address, metro, phone):
        """Заполнение персональной информации"""
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'Order_Form')]")
            )
        )

        self._fill_field("//input[@placeholder='* Имя']", name)
        self._fill_field("//input[@placeholder='* Фамилия']", lastname)
        self._fill_field("//input[@placeholder='* Адрес: куда привезти заказ']", address)
        self._select_metro(metro)
        self._fill_field("//input[@placeholder='* Телефон: на него позвонит курьер']", phone)
        self._click("//button[text()='Далее']")

    def fill_rental_details(self, date, period, color, comment=None):
        """Заполнение данных аренды"""
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[contains(@class, 'Order_Header')]"),
                "Про аренду"
            )
        )

        self._fill_field("//input[@placeholder='* Когда привезти самокат']", date)
        self._select_dropdown("//div[contains(@class, 'Dropdown-control')]", period)
        self._click(f"//input[@id='{color}']")

        if comment:
            self._fill_field("//input[@placeholder='Комментарий для курьера']", comment)

        self._click("//button[contains(text(), 'Заказать')]")

    def confirm_order(self):
        """Подтверждение заказа"""
        self._click("//button[text()='Да']")

    def get_success_message(self):
        """Получение сообщения об успешном заказе"""
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
            )
        ).text

    # Вспомогательные методы
    def _fill_field(self, xpath, value):
        """Заполнение поля с проверкой"""
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        self._scroll_to(element)
        element.clear()
        element.send_keys(value)
        time.sleep(0.3)

        if element.get_attribute('value') != value:
            raise ValueError(f"Значение в поле {xpath} не установилось")

    def _select_metro(self, station):
        """Выбор станции метро"""
        container = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'select-search')]")
            )
        )
        self._scroll_to(container)

        input_field = container.find_element(By.TAG_NAME, "input")
        input_field.click()
        time.sleep(1)

        station_xpath = f"//div[contains(@class, 'select-search__select')]//*[text()='{station}']"
        station_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, station_xpath))
        )
        self._scroll_to(station_btn)
        station_btn.click()
        time.sleep(1)

        if station not in input_field.get_attribute('value'):
            raise ValueError(f"Станция {station} не выбрана")

    def _select_dropdown(self, dropdown_xpath, option_text):
        """Выбор из выпадающего списка"""
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        self._scroll_to(dropdown)
        dropdown.click()
        time.sleep(0.5)

        option = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{option_text}']")
            )
        )
        option.click()
        time.sleep(0.5)

    def _click(self, xpath):
        """Клик по элементу"""
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        self._scroll_to(element)
        element.click()
        time.sleep(1)

    def _scroll_to(self, element):
        """Прокрутка к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.2)
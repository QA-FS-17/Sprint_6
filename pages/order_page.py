import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    @allure.step('Нажать на верхнюю кнопку "Заказать"')
    def click_order_button_top(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Нажать на нижнюю кнопку "Заказать"')
    def click_order_button_bottom(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Заполнить персональную информацию')
    def fill_personal_info(self, name, lastname, address, metro, phone):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_INPUT, lastname)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys_to_input(OrderPageLocators.METRO_STATION, metro)
        self.click_on_element((By.XPATH, f"//div[text()='{metro}']"))
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные аренды')
    def fill_rental_details(self, date, period, color, comment):
        # Заполняем дату
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)

        # Закрываем календарь кликом вне его области
        # Клик по телу страницы
        body = self.driver.find_element(By.TAG_NAME, 'body')
        body.click()

        # Ждем скрытия календаря
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        # Выбираем срок аренды
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element((By.XPATH, f"//div[text()='{period}']"))

        # Выбираем цвет
        if color == "black":
            self.click_on_element(OrderPageLocators.COLOR_BLACK)
        else:
            self.click_on_element(OrderPageLocators.COLOR_GREY)

        # Заполняем комментарий
        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)

        # Нажимаем кнопку заказа
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получить сообщение об успешном заказе')
    def get_success_message(self):
        return self.get_text_on_element(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step('Прокрутить страницу вниз')
    def scroll_to_bottom(self):
        # Сохраняем начальную позицию скролла
        initial_offset = self.driver.execute_script("return window.pageYOffset;")

        # Прокручиваем до конца
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ожидаем либо изменения позиции скролла, либо появления кнопки
        WebDriverWait(self.driver, 5).until(
            lambda d: d.execute_script("return window.pageYOffset;") > initial_offset or
                      d.find_element(*OrderPageLocators.ORDER_BUTTON_BOTTOM).is_displayed()
        )

        # Дополнительная проверка видимости кнопки
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        )
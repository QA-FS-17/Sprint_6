from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        return self

    def accept_cookies(self):
        try:
            cookie_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_btn.click()
        except:
            pass  # Если кнопки нет, продолжаем без ошибки
        return self

    def click_head_order_button(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]")
            )
        )
        self.actions.move_to_element(btn).click().perform()
        time.sleep(1)  # Даем странице загрузиться
        return self

    def scroll_and_click_foot_order_button(self):
        btn = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(0.5)

        # Кликаем через JavaScript, если обычный клик не работает
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(1)  # Даем странице загрузиться
        return self
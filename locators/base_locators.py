from selenium.webdriver.common.by import By

class BaseLocators:
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    COOKIE_BANNER = (By.ID, 'rcc-confirm-button')
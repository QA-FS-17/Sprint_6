from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локатор всего раздела вопросов
    FAQ_SECTION = (By.XPATH, '//div[@id="root"]//div[contains(@class, "Home_FAQ")]')

    # Локаторы логотипов главной страницы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # Методы для генерации локаторов вопросов и ответов
    @staticmethod
    def get_question_locator(index):
        """Возвращает локатор вопроса по индексу (0-7)"""
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def get_answer_locator(index):
        """Возвращает локатор ответа по индексу вопроса"""
        return By.ID, f"accordion__panel-{index}"

    @classmethod
    def get_all_question_locators(cls):
        return [cls.get_question_locator(i) for i in range(8)]

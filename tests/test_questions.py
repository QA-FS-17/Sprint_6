import allure
import pytest
from pages.main_page import MainPage

QUESTIONS_DATA = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. "
        "Если хотите покататься с друзьями, можете просто сделать несколько заказов — "
        "один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — "
        "всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
        "даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
        "Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
]


@allure.suite("Тесты раздела 'Вопросы о важном'")
@allure.epic("Тесты главной страницы")
@allure.feature("Проверка FAQ")
class TestQuestions:
    @allure.title("Проверка ответа на вопрос №{question_num + 1}")
    @allure.description("""
    Проверяем корректность ответа в разделе FAQ.

    **Тестовые данные:**
    - Номер вопроса: {question_num + 1}
    - Ожидаемый ответ: {expected_text}
    """)
    @pytest.mark.parametrize("question_num, expected_text", QUESTIONS_DATA,
                             ids=[f"Вопрос {i + 1}" for i in range(len(QUESTIONS_DATA))])
    def test_question_dropdown(self, driver, question_num, expected_text):
        main_page = MainPage(driver)

        with allure.step("1. Открыть главную страницу"):
            main_page.open()
            allure.attach(
                driver.get_screenshot_as_png(),
                name="main_page_open",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"2. Кликнуть на вопрос №{question_num + 1}"):
            main_page.click_question(question_num)
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"question_{question_num}_clicked",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("3. Проверить текст ответа"):
            actual_text = main_page.get_answer_text(question_num)
            allure.attach(
                f"Ожидаем: {expected_text}\nПолучено: {actual_text}",
                name="text_comparison",
                attachment_type=allure.attachment_type.TEXT
            )

            assert actual_text == expected_text, \
                f"Текст ответа не совпадает. Ожидалось: '{expected_text}', получено: '{actual_text}'"
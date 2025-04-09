# tests\test_questions.py

import pytest
import allure
from data import TestData


@allure.feature('Тесты FAQ')
class TestFAQ:
    @allure.title("Проверка ответов в FAQ")
    @pytest.mark.parametrize('index, expected', TestData.QUESTIONS_AND_ANSWERS)
    def test_faq_answers(self, main_page, index, expected):
        with allure.step("Подготовка: прокрутка к разделу FAQ"):
            main_page.scroll_to_faq_section()
            main_page.wait_for_faq_section()

        with allure.step(f"Проверка вопроса #{index}"):
            main_page.click_question(index)
            assert main_page.get_answer_text(index) == expected
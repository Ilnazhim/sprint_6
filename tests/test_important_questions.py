import allure
import pytest
from pages.main_page import MainPage
from src import urls, assertions, data


@allure.suite("Тесты по проверки текстов в блоке Вопросы о важном")
class TestQuestions:

    @pytest.mark.parametrize('answer, assert_answer', [MainPage.important_answer_1, assertions.assert_important_answer_1])
    @allure.title("Проверка текста в вопросе 1")
    def test_check_important_question_1(self, browser, answer, assert_answer):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_1()
        with allure.step("Сравнение ФР и ОР"):
            mp.assert_word(answer, assert_answer)

    @allure.title("Проверка текста в вопросе 2")
    def test_check_important_question_2(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_2()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_2() == assertions.assert_important_answer_2

    @allure.title("Проверка текста в вопросе 3")
    def test_check_important_question_3(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_3()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_3() == assertions.assert_important_answer_3

    @allure.title("Проверка текста в вопросе 4")
    def test_check_important_question_4(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_4()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_4() == assertions.assert_important_answer_4

    @allure.title("Проверка текста в вопросе 5")
    def test_check_important_question_5(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_5()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_5() == assertions.assert_important_answer_5

    @allure.title("Проверка текста в вопросе 6")
    def test_check_important_question_6(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
            browser.maximize_window()
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_6()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_6() == assertions.assert_important_answer_6

    @allure.title("Проверка текста в вопросе 7")
    def test_check_important_question_7(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
            browser.maximize_window()
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_7()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_7() == assertions.assert_important_answer_7

    @allure.title("Проверка текста в вопросе 8")
    def test_check_important_question_8(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
            browser.maximize_window()
        with allure.step("Клик на согласие с куками"):
            mp.click_accept_cookies()
        with allure.step("Клик на вопрос"):
            mp.click_important_question_8()
        with allure.step("Сравнение ФР и ОР"):
            assert mp.get_important_answer_8() == assertions.assert_important_answer_8

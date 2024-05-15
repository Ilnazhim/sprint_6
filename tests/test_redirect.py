import allure
from pages.main_page import MainPage
from src import urls


@allure.suite("Тесты с переходом по ссылкам в шапке")
class TestRedirect:

    @allure.title("Переход на главную страницу самоката при нажатии на лого Самокат")
    def test_go_to_main_page_from_logo(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
            browser.maximize_window()
        with allure.step("Клик на кнопку лого Самокат"):
            mp.click_logo_link_to_main_page()
        with allure.step("Открылась главная страница самоката"):
            mp.assert_url("https://qa-scooter.praktikum-services.ru/")

    @allure.title("Переход на главную страницу Дзен при нажатии на лого Яндекс")
    def test_go_to_yandex_from_logo(self, browser):
        with allure.step("Открытие браузера"):
            mp = MainPage(browser)
            mp.open(urls.URL)
            browser.maximize_window()
        with allure.step("Клик на кнопку лого Яндекс"):
            mp.click_logo_link_to_yandex()
        with allure.step("Переход на новую вкладку"):
            browser.switch_to.window(browser.window_handles[1])
        with allure.step("Открылась страница яндекс Дзен"):
            mp.assert_url("https://dzen.ru/?yredirect=true")

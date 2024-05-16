from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from src import urls


class RegistrationPage(BasePage):

    # Locators
    input_name = "//label[text()='Имя']/..//input"
    input_email = "//label[text()='Email']/..//input"
    input_password = "//input[@name='Пароль']"
    btn_submit = "//button[text()='Зарегистрироваться']"
    message_uncorrect_password = "//p[@class='input__error text_type_main-default']"
    btn_already_login = "//a[text()='Войти']"

    # Getters
    def get_input_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_email(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_input_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_btn_submit(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_submit)))

    def get_message_uncorrect_password(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.message_uncorrect_password)))

    def get_btn_already_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_already_login)))

    # Actions
    def input_input_name(self):
        self.get_input_name().send_keys(self.generate_name())

    def input_input_email(self):
        self.get_input_email().send_keys(self.generate_email())

    def input_input_password(self, password):
        self.get_input_password().send_keys(password)

    def click_btn_submit(self):
        self.get_btn_submit().click()

    def click_btn_already_login(self):
        self.get_btn_already_login().click()

    # Metods
    def make_registration(self, password):
        self.input_input_name()
        self.input_input_email()
        self.input_input_password(password)
        self.click_btn_submit()

    def success_registration(self):
        self.assert_url(urls.URL + urls.LOGIN_PATH)

    def failed_registration(self):
        self.assert_word(self.get_message_uncorrect_password(), 'Некорректный пароль')

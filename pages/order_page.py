import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from src import data


class OrderPage(BaseClass):

    # Locators
    input_name = "//input[@placeholder='* Имя']"
    input_surname = "//input[@placeholder='* Фамилия']"
    input_address = "//input[@placeholder='* Адрес: куда привезти заказ']"
    open_list_metro_station = "//input[@placeholder='* Станция метро']"
    select_metro_station = "//li[@data-value='1']"
    input_phone = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    input_date_arrival = "//input[@placeholder='* Когда привезти самокат']"
    open_menu_time = "//span[@class='Dropdown-arrow']"
    select_time_order = "//div[text()='сутки']"
    black_color = "//input[@id='black']"
    grey_color = "//input[@id='grey']"
    input_comment = "//input[@placeholder='Комментарий для курьера']"
    btn_next = "//button[text()='Далее']"
    btn_make_order = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    btn_accept_order = "//button[text()='Да']"

    # Getters
    def get_input_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_name)))

    def get_input_surname(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_surname)))

    def get_input_address(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_address)))

    def get_open_list_metro_station(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_list_metro_station)))

    def get_select_metro_station(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_metro_station)))

    def get_input_phone(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_date_arrival(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_date_arrival)))

    def get_open_menu_time(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.open_menu_time)))

    def get_select_time_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_time_order)))

    def get_black_color(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.black_color)))

    def get_grey_color(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.grey_color)))

    def get_input_comment(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_comment)))

    def get_btn_next(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_next)))

    def get_btn_make_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_make_order)))

    def get_btn_accept_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_accept_order)))

    # Actions
    def input_input_name(self):
        self.get_input_name().send_keys(data.name)

    def input_input_surname(self):
        self.get_input_surname().send_keys(data.surname)

    def input_input_address(self):
        self.get_input_address().send_keys(data.address)

    def click_open_list_metro_station(self):
        self.get_open_list_metro_station().click()

    def click_select_metro_station(self):
        self.get_select_metro_station().click()

    def input_input_phone(self, phone):
        self.get_input_phone().send_keys(phone)

    def input_input_date_arrival(self):
        self.get_input_date_arrival().send_keys(data.date_arrival)

    def click_open_menu_time(self):
        self.get_open_menu_time().click()

    def click_select_time_order(self):
        self.get_select_time_order().click()

    def click_black_color(self):
        self.get_black_color().click()

    def click_grey_color(self):
        self.get_grey_color().click()

    def input_input_comment(self):
        self.get_input_comment().send_keys(data.comment)

    def click_btn_next(self):
        self.get_btn_next().click()

    def click_btn_make_order(self):
        self.get_btn_make_order().click()

    def click_btn_accept_order(self):
        self.get_btn_accept_order().click()

    # Metods
    def fill_form_order_black_samocat(self, phone):
        with allure.step("Заполение формы заказа с черным самокатом"):
            self.input_input_name()
            self.input_input_surname()
            self.input_input_address()
            self.click_open_list_metro_station()
            self.click_select_metro_station()
            self.input_input_phone(phone)
            self.click_btn_next()
            self.input_input_date_arrival()
            self.click_open_menu_time()
            self.click_select_time_order()
            self.click_black_color()
            self.input_input_comment()
            self.click_btn_make_order()
            self.click_btn_accept_order()

    def fill_form_order_grey_samocat(self, phone):
        with allure.step("Заполение формы заказа с серым самокатом"):
            self.input_input_name()
            self.input_input_surname()
            self.input_input_address()
            self.click_open_list_metro_station()
            self.click_select_metro_station()
            self.input_input_phone(phone)
            self.click_btn_next()
            self.input_input_date_arrival()
            self.click_open_menu_time()
            self.click_select_time_order()
            self.click_black_color()
            self.input_input_comment()
            self.click_btn_make_order()
            self.click_btn_accept_order()

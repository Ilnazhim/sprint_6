from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class MainPage(BasePage):

    # Locators
    accept_cookies = "//button[@id='rcc-confirm-button']"
    logo_link_to_main_page = "//a[@class='Header_LogoScooter__3lsAR']"
    logo_link_to_yandex = "//a[@class='Header_LogoYandex__3TSOI']"

    important_question_1 = "//div[@id='accordion__heading-0']"
    important_question_2 = "//div[@id='accordion__heading-1']"
    important_question_3 = "//div[@id='accordion__heading-2']"
    important_question_4 = "//div[@id='accordion__heading-3']"
    important_question_5 = "//div[@id='accordion__heading-4']"
    important_question_6 = "//div[@id='accordion__heading-5']"
    important_question_7 = "//div[@id='accordion__heading-6']"
    important_question_8 = "//div[@id='accordion__heading-7']"

    important_answer_1 = "//div[@id='accordion__panel-0']//p"
    important_answer_2 = "//div[@id='accordion__panel-1']//p"
    important_answer_3 = "//div[@id='accordion__panel-2']//p"
    important_answer_4 = "//div[@id='accordion__panel-3']//p"
    important_answer_5 = "//div[@id='accordion__panel-4']//p"
    important_answer_6 = "//div[@id='accordion__panel-5']//p"
    important_answer_7 = "//div[@id='accordion__panel-6']//p"
    important_answer_8 = "//div[@id='accordion__panel-7']//p"

    btn_header_order = "//button[@class='Button_Button__ra12g']"
    btn_footer_order = "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"

    # Getters
    def get_accept_cookies(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookies)))

    def get_logo_link_to_main_page(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_link_to_main_page)))

    def get_logo_link_to_yandex(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_link_to_yandex)))

    def get_important_question_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_1)))

    def get_important_question_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_2)))

    def get_important_question_3(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_3)))

    def get_important_question_4(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_4)))

    def get_important_question_5(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_5)))

    def get_important_question_6(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_6)))

    def get_important_question_7(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_7)))

    def get_important_question_8(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_question_8)))

    def get_important_answer_1(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_1))).text

    def get_important_answer_2(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_2))).text

    def get_important_answer_3(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_3))).text

    def get_important_answer_4(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_4))).text

    def get_important_answer_5(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_5))).text

    def get_important_answer_6(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_6))).text

    def get_important_answer_7(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_7))).text

    def get_important_answer_8(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.important_answer_8))).text

    def get_btn_header_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_header_order)))

    def get_btn_footer_order(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.btn_footer_order)))

    # Actions
    def click_accept_cookies(self):
        self.get_accept_cookies().click()

    def click_logo_link_to_main_page(self):
        self.get_logo_link_to_main_page().click()

    def click_logo_link_to_yandex(self):
        self.get_logo_link_to_yandex().click()

    def click_important_question_1(self):
        self.get_important_question_1().click()

    def click_important_question_2(self):
        self.get_important_question_2().click()

    def click_important_question_3(self):
        self.get_important_question_3().click()

    def click_important_question_4(self):
        self.get_important_question_4().click()

    def click_important_question_5(self):
        self.get_important_question_5().click()

    def click_important_question_6(self):
        self.get_important_question_6().click()

    def click_important_question_7(self):
        self.get_important_question_7().click()

    def click_important_question_8(self):
        self.get_important_question_8().click()

    def click_btn_header_order(self):
        self.get_btn_header_order().click()

    def click_btn_footer_order(self):
        self.get_btn_footer_order().click()

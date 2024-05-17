from selenium.webdriver.common.by import By
from base.base_page import BasePage


class MainPage(BasePage):

    # Locators
    accept_cookies = By.XPATH, "//button[@id='rcc-confirm-button']"
    logo_link_to_main_page = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    logo_link_to_yandex = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"

    important_question_1 = By.XPATH, "//div[@id='accordion__heading-0']"
    important_question_2 = By.XPATH, "//div[@id='accordion__heading-1']"
    important_question_3 = By.XPATH, "//div[@id='accordion__heading-2']"
    important_question_4 = By.XPATH, "//div[@id='accordion__heading-3']"
    important_question_5 = By.XPATH, "//div[@id='accordion__heading-4']"
    important_question_6 = By.XPATH, "//div[@id='accordion__heading-5']"
    important_question_7 = By.XPATH, "//div[@id='accordion__heading-6']"
    important_question_8 = By.XPATH, "//div[@id='accordion__heading-7']"

    important_answer_1 = By.XPATH, "//div[@id='accordion__panel-0']//p"
    important_answer_2 = By.XPATH, "//div[@id='accordion__panel-1']//p"
    important_answer_3 = By.XPATH, "//div[@id='accordion__panel-2']//p"
    important_answer_4 = By.XPATH, "//div[@id='accordion__panel-3']//p"
    important_answer_5 = By.XPATH, "//div[@id='accordion__panel-4']//p"
    important_answer_6 = By.XPATH, "//div[@id='accordion__panel-5']//p"
    important_answer_7 = By.XPATH, "//div[@id='accordion__panel-6']//p"
    important_answer_8 = By.XPATH, "//div[@id='accordion__panel-7']//p"

    btn_header_order = By.XPATH, "//button[@class='Button_Button__ra12g']"
    btn_footer_order = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"

    def click_accept_cookies(self):
        self.click_element(self.accept_cookies)

    def click_logo_link_to_main_page(self):
        self.click_element(self.logo_link_to_yandex)

    def click_logo_link_to_yandex(self):
        self.click_element(self.logo_link_to_yandex)

    def click_important_question_1(self):
        self.click_element(self.important_question_1)

    def click_important_question_2(self):
        self.click_element(self.important_question_2)

    def click_important_question_3(self):
        self.click_element(self.important_question_3)

    def click_important_question_4(self):
        self.click_element(self.important_question_4)

    def click_important_question_5(self):
        self.click_element(self.important_question_5)

    def click_important_question_6(self):
        self.click_element(self.important_question_6)

    def click_important_question_7(self):
        self.click_element(self.important_question_7)

    def click_important_question_8(self):
        self.click_element(self.important_question_8)

    def click_btn_header_order(self):
        self.click_element(self.btn_header_order)

    def click_btn_footer_order(self):
        self.click_element(self.btn_footer_order)

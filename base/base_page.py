from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        """Method open browser"""
        self.browser.get(url)
        self.url = url

    def get_element(self, how, variable):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, variable)))


    def get_current_url(self):
        """Method get current url"""
        return self.browser.current_url

    @staticmethod
    def assert_word(word, result):
        """Method assert word"""
        value_word = word.text
        value_result = result
        print(value_word)
        assert value_word == value_result

    def is_element_present(self, how, what):
        """Method is element present"""
        try:
            WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((how, what)))
        except NoSuchElementException:
            return False
        return True

    def assert_url(self, result):
        """Method assert url"""
        get_url = self.browser.current_url
        assert get_url == result

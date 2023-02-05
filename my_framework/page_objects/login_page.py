from selenium.webdriver.common.by import By

from my_framework.page_objects.python_page import PythonPage
from my_framework.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __login_input = (By.XPATH, '//input[@name="wpName"]')
    __password_input = (By.XPATH, '//input[@name="wpPassword"]')
    __login_button = (By.XPATH, '//div/button')
    __title = 'Вхід до системи — Вікіпедія'
    __message_invalid_login_details = (By.XPATH, '//div[contains(@class, "mw-message-box-error")]')
    __left_menu = (By.XPATH, '//div[@id="mw-panel"]')
    __header = (By.XPATH, '//div[@id="mw-head"]')
    __checkbox_remember_me = (By.XPATH, '//input[@name = "wpRemember"]')

    def set_login(self, login):
        self._send_keys(self.__login_input, login)
        return self

    def set_password(self, password):
        self._send_keys(self.__password_input, password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)

    def login(self, login, password):
        self.set_login(login).set_password(password).click_login_button()
        return PythonPage(self.driver)

    def is_title(self):
        return self._is_title(self.__title)

    def check_not_valid_login_data(self):
        return self._is_visible(self.__message_invalid_login_details)

    def is_left_menu_visible(self):
        return self._is_visible(self.__left_menu)

    def is_header_visible(self):
        return self._is_visible(self.__header)


from selenium.webdriver.common.by import By

from my_framework.utilities.web_ui.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Скинути пароль — Вікіпедія'
    __left_menu = (By.XPATH, '//div[@id="mw-panel"]')
    __name_input = (By.XPATH, '//div//input[@name="wpUsername"]')
    __email_address = (By.XPATH, '//div//input[@name="wpEmail"]')
    __reset_password_button = (By.XPATH, '//button//span[@class="oo-ui-labelElement-label"]')

    def is_title(self):
        return self._is_title(self.__title)

    def is_left_menu_visible(self):
        return self._is_visible(self.__left_menu)

    def is_name_input_visible(self):
        return self._is_visible(self.__name_input)

    def is_email_address_input_visible(self):
        return self._is_visible(self.__name_input)

    def is_reset_password_button_clickable(self):
        return self._is_clickable(self.__reset_password_button)
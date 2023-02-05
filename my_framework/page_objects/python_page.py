from selenium.webdriver.common.by import By

from my_framework.utilities.web_ui.base_page import BasePage


class PythonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_locator = (By.XPATH, '//li[@id="pt-userpage"]//span')
    __content_menu = (By.XPATH, '//div[@role="navigation"]')
    __article_title = (By.XPATH, '//span[@class="mw-page-title-main"]')
    __page_url = 'https://uk.wikipedia.org/wiki/Python'
    __title_Python_page = 'Python — Вікіпедія'


    def is_login_visible(self):
        return self._is_visible(self.__user_locator)

    def is_clickable_name(self):
        return self._is_clickable(self.__user_locator)

    def is_title(self):
        return self._is_title(self.__title_Python_page)

    def is_content_menu_visible(self):
        return self._is_visible(self.__content_menu)

    def is_article_title(self, text):
        return self.is_text_in_page(self.__article_title, text)

    def is_check_url(self):
        return self.is_url_to_be(self.__page_url)

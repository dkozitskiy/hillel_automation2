from selenium.webdriver.common.by import By
from my_framework.utilities.config_parser import ReadConfig

from my_framework.utilities.web_ui.base_page import BasePage


class CommunityPortal(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Вікіпедія:Портал спільноти — Вікіпедія'
    __menu_container = (By.XPATH, '//div[@id="menu-container"]')
    __lock = (By.XPATH, '//div[@id="menu-container"]')
    __how_to_help = (By.XPATH, '//td[@rowspan="3"]')
    __assist_and_social_life = (By.XPATH, '//td[@colspan="2"] //h2[@class="ext-discussiontools-init-section"]/..')

    def is_title(self):
        return self._is_title(self.__title)

    def is_visible_menu_container(self):
        return self._is_visible(self.__menu_container)

    def is_lock_visible(self):
        return self._is_visible(self.__lock)

    def is_how_to_help_visible(self):
        return self._is_visible(self.__how_to_help)

    def is_assist_and_social_life_visible(self):
        return self._is_visible(self.__assist_and_social_life)

    def is_check_url(self, env):
        return self.is_url_to_be(env)

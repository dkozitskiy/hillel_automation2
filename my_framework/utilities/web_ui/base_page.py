from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 20)

    def __wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __text_to_be_present(self, locator, text):
        return self.__wait.until(EC.text_to_be_present_in_element(locator, text))

    def __wait_until_element_to_be_selected(self, locator):
        return self.__wait.until(EC.element_to_be_selected(locator))

    def __wait_until_url_to_be(self, url):
        return self.__wait.until(EC.url_to_be(url))

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _is_clickable(self, locator):
        try:
            self.__wait_until_element_clickable(locator)
            return True
        except TimeoutException:
            return False

    def _click(self, locator):
        element = self.__wait_until_element_clickable(locator)
        element.click()

    def _is_title(self, title):
        if self._driver.title == title:
            return True
        return False

    def is_text_in_page(self, locator, text):
        try:
            self.__text_to_be_present(locator, text)
            return True
        except TimeoutException:
            return False

    def is_url_to_be(self, url):
        try:
            self.__wait_until_url_to_be(url)
            return True
        except TimeoutException:
            return False



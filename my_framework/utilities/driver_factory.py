from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id):
        if int(driver_id) == DriverFactory.CHROME:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)

            driver = Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)
        elif int(driver_id) == DriverFactory.FIREFOX:
            driver = Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif int(driver_id) == DriverFactory.EDGE:
            driver = Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver

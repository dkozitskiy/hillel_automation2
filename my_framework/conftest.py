import json
import pytest

from my_framework.data.gender import Gender
from my_framework.CONSTANTS import ROOT_DIR
from my_framework.page_objects.community_portal import CommunityPortal
from my_framework.page_objects.home_page import HomePage
from my_framework.page_objects.login_page import LoginPage
from my_framework.page_objects.reset_password_page import ResetPasswordPage
from my_framework.utilities.configuration import Configuration
from my_framework.utilities.driver_factory import DriverFactory



@pytest.fixture(scope="session")
def env():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def create_driver(env):
    driver = DriverFactory.create_driver(env.browser_id)
    # driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver, env):
    create_driver.get(env.base_url)
    return LoginPage(create_driver)


@pytest.fixture()
def open_reset_password_page(create_driver, env):
    create_driver.get(env.reset_password_page_url)
    return ResetPasswordPage(create_driver)


@pytest.fixture()
def open_home_page(create_driver, env):
    create_driver.get(env.start_page)
    return HomePage(create_driver)


@pytest.fixture()
def open_community_portal(create_driver, env):
    create_driver.get(env.community_portal_url)
    return CommunityPortal(create_driver)


@pytest.fixture()
def create_gender():
    return Gender()

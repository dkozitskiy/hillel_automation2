import configparser

from my_framework.CONSTANTS import ROOT_DIR

abs_path = '/home/denis/Python/hillel_automation/my_framework/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_start_page():
        return config.get('app_info', 'start_page')

    @staticmethod
    def get_community_portal_page():
        return config.get('app_info', 'community_portal_url')

    @staticmethod
    def reset_password_page_url():
        return config.get('app_info', 'reset_password_page_url')

    @staticmethod
    def get_login():
        return config.get('user_data', 'login')

    @staticmethod
    def get_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser_data', 'browser_id')




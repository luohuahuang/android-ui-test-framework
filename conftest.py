import pytest
import datetime
import os

from appium import webdriver
from helpers import ensure_dir

import actions


def pytest_configure(config):
    if not hasattr(config, "slaveinput"):
        current_day = (datetime.datetime.now().strftime("%Y_%m_%d_%H_%S"))
        ensure_dir("results")
        ensure_dir(os.path.join("results", current_day))
        result_dir = os.path.join(os.path.dirname(__file__), "results", current_day)
        ensure_dir(result_dir)
        result_dir_test_run = result_dir
        ensure_dir(os.path.join(result_dir_test_run, "screenshots"))
        ensure_dir(os.path.join(result_dir_test_run, "logcat"))
        config.screen_shot_dir = os.path.join(result_dir_test_run, "screenshots")
        config.logcat_dir = os.path.join(result_dir_test_run, "logcat")

class DeviceLogger:
    def __init__(self, logcat_dir, screenshot_dir):
        self.screenshot_dir = screenshot_dir
        self.logcat_dir = logcat_dir


@pytest.fixture(scope="session")
def device_logger(request):
    logcat_dir = request.config.logcat_dir
    screenshot_dir = request.config.screen_shot_dir
    return DeviceLogger(logcat_dir, screenshot_dir)


APPIUM_URL = os.getenv('APPIUM_URL') if os.getenv('APPIUM_URL') else 'http://localhost:4723/wd/hub'

APP_PATH = os.getenv('APP_PATH') if os.getenv('APP_PATH') \
    else '/Users/huanglh/Downloads/' \
         'xxx.apk'

PLATFORM_VERSION = os.getenv('PLATFORM_VERSION') if os.getenv('PLATFORM_VERSION') else '7.1.1'


@pytest.fixture(scope="function")
def driver(request):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': PLATFORM_VERSION,
        'deviceName': 'Android Emulator',
        'app': APP_PATH,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'deviceName': 'T21718CJ40232',
        # 'dontStopAppOnReset': True
        # 'autoGrantPermissions': True,
    }
    driver = webdriver.Remote(APPIUM_URL, desired_caps)
    driver.implicitly_wait(5)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver  # provide the fixture value


@pytest.fixture(scope="function")
def prepare_for_bills(driver):
    actions.login.log_in_as_owner(driver)
    actions.open_bills.navigate_to_open_bills(driver)
    actions.open_bills.switch_open_bills(driver, should_enable=True)
    actions.open_bills.switch_table_management(driver, should_enable=True)
    actions.base.back_to_main_panel(driver)
    actions.cash_drawer.navigate_to_cash_drawer_panel(driver, should_navigate_to=True)
    actions.cash_drawer.navigate_to_cash_drawer_setting_panel(driver, should_navigate_to=False)
    actions.cash_drawer.disable_cash_drawer(driver)
    actions.base.back_to_main_panel(driver)


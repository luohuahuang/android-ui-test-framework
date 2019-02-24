from selenium.common.exceptions import NoSuchElementException, WebDriverException

from paths import xxx_paths as PATH
from labels import xxx_labels as LABEL
from configs import xxx_configs as CONFIG
from appium.webdriver import Remote


class BaseAction(object):

    def click_system_tray(self, driver):
        el = driver.find_element_by_id(PATH.DOCK_SYSTEM_TRAY)
        el.click()

    def click_menu_tray(self, driver):
        el = driver.find_element_by_android_uiautomator(PATH.DOCK_MENU_TRAY)
        el.click()



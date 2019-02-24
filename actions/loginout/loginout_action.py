import re
from configs import xxx_configs as CONFIG
from labels import xxx_labels as LABEL
from paths import xxx_paths as PATH

from time import sleep
from selenium.common.exceptions import NoSuchElementException

from actions.base.base_action import BaseAction

from appium.webdriver import Remote


class LogInOutAction(BaseAction):

    @staticmethod
    def log_in_as_owner(self, driver: Remote, does_account_exist=True, is_correct_password=True):
        self._initial_sign_in_click(self, driver)

import actions
from configs import xxx_configs as CONFIG
import pytest


class TestXXXLogin:
    def test_owner_log_in_out(self, driver):
        actions.login.log_in_as_owner(driver)
        actions.login.log_out(driver, True)
        actions.login.log_in_as_owner(driver)

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
    def _initial_sign_in_click(self, driver):
        for _ in range(0, 10):
            sleep(1)
            try:
                el = driver.find_element_by_id(PATH.LOGIN_PAGE_SIGN_IN_BUTTON)
                el.click()
            except NoSuchElementException:
                continue
            break

    def log_in_as_owner(self, driver: Remote, does_account_exist=True, is_correct_password=True):
        self._initial_sign_in_click(self, driver)

        sign_in_next_btn = driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_NEXT_BUTTON)
        assert LABEL.NEXT.upper() == sign_in_next_btn.text.upper()

        if does_account_exist is False:
            driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_INPUT).send_keys(CONFIG.NOT_EXIST_OWNER_ACCOUNT)
            sign_in_next_btn.click()
            assert LABEL.CREATE_NEW_ACCOUNT == driver.find_element_by_id(
                PATH.CREATE_NEW_ACCOUNT_TEXT).text
            assert LABEL.CREATE_NEW_ACCOUNT_HINT == driver.find_element_by_id(
                PATH.CREATE_NEW_ACCOUNT_HINT).text
            return

        if is_correct_password is False:
            driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_INPUT).send_keys(CONFIG.OWNER_ACCOUNT)
            sign_in_next_btn.click()
            driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_SMS_CODE_INPUT).send_keys(CONFIG.WRONG_SMS_CODE)
            sms_next_btn = driver.find_element_by_id(PATH.OWNER_SIGN_IN_BUTTON)
            sms_next_btn.click()
            el = driver.find_element_by_id(PATH.COMMON_YES_POSITIVE_BUTTON)
            el.click()
            return
        else:
            driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_INPUT).send_keys(CONFIG.OWNER_ACCOUNT)
            sign_in_next_btn.click()
            sign_in_text = driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_TEXT).text
            assert LABEL.SIGN_IN.upper() == sign_in_text.upper()
            resend_text = driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_RESEND_HINT_TEXT)
            assert re.compile(LABEL.RESEND_CODE).search(resend_text.text) is not None
            sms_text = driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_SMS_HINT_TEXT).text
            assert LABEL.SIGN_IN_SMS_HINT.format(CONFIG.OWNER_ACCOUNT) == sms_text

        driver.find_element_by_id(PATH.OWNER_SIGN_IN_PAGE_SMS_CODE_INPUT).send_keys(CONFIG.DEFAULT_SMS_CODE)
        sms_next_btn = driver.find_element_by_id(PATH.OWNER_SIGN_IN_BUTTON)
        assert LABEL.NEXT.upper() == sms_next_btn.text.upper()
        sms_next_btn.click()
        sleep(3)

    def log_out(self, driver, is_log_out=True):
        BaseAction.click_system_tray(self, driver)
        BaseAction.navigate_to_settings_panel(self, driver)
        el0 = driver.find_element_by_id(PATH.SIGN_OUT_BUTTON)
        el0.click()
        el = driver.find_element_by_id(PATH.SIGN_OUT_CONFIRM_TEXT)
        assert LABEL.CONFIRM_SIGN_OUT == el.text
        if is_log_out:
            el1 = driver.find_element_by_id(PATH.COMMON_YES_POSITIVE_BUTTON)
            el1.click()
        else:
            el2 = driver.find_element_by_id(PATH.COMMON_NO_NEGATIVE_BUTTON)
            el2.click()

    def log_in_as_staff(self, driver, account, is_correct_owner=True,
                        is_correct_password=True, is_customized_password=False):
        self._initial_sign_in_click(self, driver)
        el1 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_BUTTON)
        el1.click()
        el2 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_OWNER_MOBILE_INPUT)
        el2.click()
        if is_correct_owner is False:
            el2.send_keys(CONFIG.NOT_EXIST_OWNER_ACCOUNT)
        else:
            el2.send_keys(CONFIG.OWNER_ACCOUNT)
        el3 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_USERNAME_INPUT)
        el3.click()
        el3.send_keys(account)
        el4 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_PASSWORD_INPUT)
        el4.click()
        if is_customized_password:
            el4.send_keys(CONFIG.CUSTOMIZED_PASSWORD)
        else:
            if is_correct_password is False:
                el4.send_keys(CONFIG.WRONG_PASSWORD)
            else:
                el4.send_keys(CONFIG.DEFAULT_PASSWORD)
        el5 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_NEXT_BUTTON)
        el5.click()
        sleep(2)
        if is_correct_password is False or is_correct_owner is False:
            el6 = driver.find_element_by_id(PATH.STAFF_SIGN_IN_NEXT_BUTTON)
            assert el6 is not None
        else:
            pass # no need to check


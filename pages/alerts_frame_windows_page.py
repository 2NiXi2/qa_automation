import random
import time

import allure
from selenium.common import UnexpectedAlertPresentException

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators

    @allure.step('Check opened new tab and window')
    def check_opened_new_tab(self, arg):
        with allure.step('Check opened new tab'):
            if arg == 'tab':
                self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
                self.switch_tab(1)
                text_title = self.element_is_present(self.locators.TITLE_NEW).text
                self.switch_tab(0)
                return text_title

        with allure.step('Check opened new window'):
            if arg == 'window':
                self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
                self.switch_tab(1)
                text_title = self.element_is_present(self.locators.TITLE_NEW).text
                self.switch_tab(0)
                return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators

    @allure.step('Get text from alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('Check alert appear after 5 sec')
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5.5)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    @allure.step('Check confirm alert')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('Check prompt alert')
    def check_prompt_alert(self):
        text = f'We need it with {random.randint(0, 999999)} times'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text_result, text


class FramesPage(BasePage):
    locators = FramesPageLocators

    @allure.step('check frame')
    def check_frame(self, frame_num):
        with allure.step('Check frame number 1'):
            if frame_num == 'frame1':
                frame = self.element_is_present(self.locators.FIRST_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.switch_frame(frame)
                text = self.element_is_present(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
                return [text, width, height]
        with allure.step('Check frame number 2'):
            if frame_num == 'frame2':
                frame = self.element_is_present(self.locators.SECOND_FRAME)
                width = frame.get_attribute('width')
                height = frame.get_attribute('height')
                self.switch_frame(frame)
                text = self.element_is_present(self.locators.TITLE_FRAME).text
                self.driver.switch_to.default_content()
                return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators

    @allure.step('Check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self, key):
        with allure.step('Check small modal dialog'):
            if key == 'small':
                self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
                title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
                body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
                self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
                return [title_small, len(body_small_text)]

        with allure.step('Check large modal dialog'):
            if key == 'large':
                self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
                title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
                body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
                self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
                return [title_large, len(body_large_text)]

import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_page import BasePage


class DynamicPropertiesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/dynamic-properties')
        self.enable_btn = Button(driver, (By.XPATH, '//*[@id="enableAfter"]'))
        self.color_change_btn = Button(driver, (By.XPATH, '//*[@id="colorChange"]'))
        self.visible_after_5_sec_btn = Button(driver, (By.XPATH, '//*[@id="visibleAfter"]'))

    def check_enable_button(self):
        try:
            self.enable_btn.is_clickable()
        except TimeoutException:
            return False
        return True

    def check_changed_of_color(self):
        self.color_change_btn.is_present()
        color_btn_before = self.color_change_btn.value_of_css_property('color')
        time.sleep(5.5)
        color_btn_after = self.color_change_btn.value_of_css_property('color')
        return color_btn_before, color_btn_after

    def check_appear_button(self):
        try:
            self.visible_after_5_sec_btn.is_visible()
        except TimeoutException:
            return False
        return True

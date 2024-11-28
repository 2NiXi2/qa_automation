import random
import time

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from pages.base_page import BasePage


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/alerts')
        self.see_alert = Button(driver, (By.XPATH, '//*[@id="alertButton"]'))
        self.alert_5_sec = Button(driver, (By.XPATH, '//*[@id="timerAlertButton"]'))
        self.confirm = Button(driver, (By.XPATH, '//*[@id="confirmButton"]'))
        self.confirm_result = TextField(driver, (By.XPATH, '//*[@id="confirmResult"]'))
        self.prompt_box = Button(driver, (By.XPATH, '//*[@id="confirmButton"]'))
        self.prompt_box_result = TextField(driver, (By.XPATH, '//*[@id="promptResult"]'))

    def check_see_alert(self):
        self.see_alert.is_visible().click()
        alert = self.driver.switch_to.alert
        return alert.text

    def check_alert_appear_5_sec(self):
        self.alert_5_sec.is_visible().click()
        time.sleep(5.5)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.confirm.is_visible().click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        self.confirm_result.is_present()
        text_result = self.confirm_result.text()
        return text_result

    def check_prompt_alert(self):
        text = f'We need somebody to know {random.randint(0, 1164146485496448484964)}'
        self.prompt_box.is_visible().click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.prompt_box_result.is_present().text()
        return text_result, text
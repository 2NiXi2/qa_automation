import random
import time

from selenium.webdriver.common.by import By

from elements.button import Button
from elements.slider import Slider
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.progress_bar_btn = Button(driver, (By.XPATH, '//*[@id="startStopButton"]'))
        self.progress_bar_value = Slider(driver, (By.XPATH, '//*[@id="progressBar"]/div'))

    def change_progress_bar_value(self):
        self.progress_bar_value.is_present()
        value_before = self.progress_bar_value.text()
        self.progress_bar_btn.is_clickable()
        self.progress_bar_btn.click()
        time.sleep(random.randint(2, 8))
        self.progress_bar_btn.click()
        value_after = self.progress_bar_value.text()
        return value_before, value_after

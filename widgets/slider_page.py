from selenium.webdriver.common.by import By

from elements.slider import Slider
from pages.base_page import BasePage
import random


class SliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/slider')
        self.slider_input = Slider(driver, (By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input'))
        self.slider_value = Slider(driver, (By.XPATH, '//*[@id="sliderValue"]'))

    def change_slider_value(self):
        value_before = self.slider_value.is_visible().get_attribute('value')
        drag = self.slider_input.is_visible()
        self.action_drag_and_drop_by_offset(drag, random.randint(0, 100), 0)
        value_after = self.slider_value.is_visible().get_attribute('value')
        return value_before, value_after
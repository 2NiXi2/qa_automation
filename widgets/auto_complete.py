import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.text_field import TextField
from generator.generator import generated_color
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/auto-complete')
        self.multi_input = TextField(driver, (By.XPATH, '//*[@id="autoCompleteMultipleInput"]'))
        self.multi_value = TextField(driver, (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]'))
        self.multi_value_remove = TextField(driver, (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path'))

        self.single_value = TextField(driver, (By.XPATH, '//*[@id="autoCompleteSingleContainer"]/div/div[1]/div[1]'))
        self.single_input = TextField(driver, (By.XPATH, '//*[@id="autoCompleteSingleInput"]'))

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 10))
        for color in colors:
            self.multi_input.is_clickable()
            self.multi_input.type(color)
            self.multi_input.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        cnt_value_before = self.multi_value.are_visible()
        remove_btn_list = self.multi_value_remove.are_visible()
        for value in remove_btn_list:
            value.click()
            break
        cnt_value_after = len(self.multi_value.are_visible())
        return cnt_value_before, cnt_value_after

    def check_color_in_multi(self):
        color_list = self.multi_value.are_present()
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        self.single_input.is_present()
        self.single_input.send_keys(color)
        self.single_input.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.single_value.is_visible()
        return color.text

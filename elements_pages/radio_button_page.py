from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from pages.base_page import BasePage


class RadioButtonPageCheck(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/radio-button')
        self.yes_button = Button(driver, (By.XPATH, "//label[starts-with(@class, 'custom-control')"
                                                    "and @for='yesRadio']"))
        self.no_button = Button(driver, (By.XPATH, "//label[starts-with(@class, 'custom-control')"
                                                   "and @for='noRadio']"))
        self.impressive_button = Button(driver, (By.XPATH, "//label[starts-with(@class, 'custom-control')"
                                                           "and @for='impressiveRadio']"))
        self.output_result = TextField(driver, (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p/span'))

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.yes_button,
            'impressive': self.impressive_button,
            'no': self.no_button,
        }
        choices[choice]()

    def get_output_result(self):
        return self.output_result.text()
from selenium.webdriver.common.by import By

from elements.frame import Frame
from pages.base_page import BasePage


class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/frames')
        self.first_frame = Frame(driver, (By.XPATH, '//*[@id="frame1"]'))
        self.second_frame = Frame(driver, (By.XPATH, '//*[@id="frame2"]'))
        self.title_frame = Frame(driver, (By.XPATH, '//*[@id="sampleHeading"]'))

    def check_frame(self, value):
        if value == 'frame1':
            self.first_frame.is_present()
            width = self.first_frame.get_attribute('width')
            height = self.first_frame.get_attribute('height')
            self.switch_frame(value)
            self.title_frame.is_present()
            text = self.title_frame.text()
            self.driver.switch_to.default_content()
            return [text, width, height]
        elif value == 'frame2':
            self.second_frame.is_present()
            width = self.second_frame.get_attribute('width')
            height = self.second_frame.get_attribute('height')
            self.switch_frame(value)
            self.title_frame.is_present()
            text = self.title_frame.text()
            self.driver.switch_to.default_content()
            return [text, width, height]

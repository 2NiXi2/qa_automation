from selenium.webdriver.common.by import By

from elements.frame import Frame
from elements.text_field import TextField
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/nestedframes')
        self.parent_fr = Frame(driver, (By.XPATH, '//*[@id="frame1"]'))
        self.parent_txt = TextField(driver, (By.XPATH, '/html/body'))
        self.child_fr = Frame(driver, (By.XPATH, '/html/body/iframe'))
        self.child_txt = TextField(driver, (By.CSS_SELECTOR, 'p'))

    def check_nested_frames(self):
        parent = self.parent_fr.is_present()
        self.switch_frame(parent)
        self.parent_txt.is_present()
        parent_text = self.parent_txt.text()
        child = self.child_fr.is_present()
        self.switch_frame(child)
        self.child_txt.is_present()
        child_text = self.child_txt.text()
        return parent_text, child_text
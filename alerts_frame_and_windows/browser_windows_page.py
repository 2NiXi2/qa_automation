from selenium.webdriver.common.by import By

from elements.button import Button
from elements.pop_up import PopUp
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/browser-windows')
        self.new_tab = Button(driver, (By.XPATH, '//*[@id="tabButton"]'))
        self.new_window = Button(driver, (By.XPATH, '//*[@id="windowButton"]'))
        self.title_new = PopUp(driver, (By.XPATH, '//*[@id="sampleHeading"]'))

    def check_frame(self, value):
        if value == 'tab':
            self.new_tab.is_visible().click()
            self.switch_tab(1)
            self.title_new.is_present()
            title = self.title_new.text()
            self.switch_tab(0)
            return title
        elif value == 'window':
            self.new_window.is_visible().click()
            self.switch_tab(1)
            self.title_new.is_present()
            title = self.title_new.text()
            self.switch_tab(0)
            return title
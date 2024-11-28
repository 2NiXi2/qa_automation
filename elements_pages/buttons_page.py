from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from pages.base_page import BasePage


class ButtonsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/buttons')
        #buttons
        self.double_click = Button(driver, (By.XPATH, '//*[@id="doubleClickBtn"]'))
        self.right_click = Button(driver, (By.XPATH, '//*[@id="rightClickBtn"]'))
        self.dynamic_click = Button(driver, (By.XPATH, '//div[3]/button'))

        #results
        self.double_scs = TextField(driver, (By.XPATH, '//*[@id="doubleClickMessage"]'))
        self.right_click_scs = TextField(driver, (By.XPATH, '//*[@id="rightClickMessage"]'))
        self.dynamic_click_scs = TextField(driver, (By.XPATH, '//*[@id="dynamicClickMessage"]'))

    def click_on_different_button(self, click):
        if click == 'double':
            self.double_click.is_visible()
            self.double_click.action_double_click()
            return self.check_clicked_on_the_button(self.double_scs)
        elif click == 'right':
            self.right_click.is_visible()
            self.right_click.action_right_click()
            return self.check_clicked_on_the_button(self.right_click_scs)
        elif click == 'dynamic':
            self.dynamic_click.is_visible()
            self.dynamic_click.click()
            return self.check_clicked_on_the_button(self.dynamic_click_scs)
        else:
            ValueError ("Некорректный тип клика. Используйте: 'double', 'right', 'dynamic'.")

    def check_clicked_on_the_button(self, element):
        element.is_present()
        return element.text()

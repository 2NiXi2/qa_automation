from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from elements.title import Title
from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/modal-dialogs')
        self.small_modal_btn = Button(driver, (By.XPATH, '//*[@id="showSmallModal"]'))
        self.small_modal_close_btn = Button(driver, (By.XPATH, '//*[@id="closeSmallModal"]'))
        self.body_small_modal = TextField(driver, (By.XPATH, '//*[@class="modal-body"]'))
        self.title_small_modal = Title(driver, (By.XPATH, '//*[@id="example-modal-sizes-title-sm"]'))

        self.large_modal_btn = Button(driver, (By.XPATH, '//*[@id="showLargeModal"]'))
        self.large_modal_close_bnt = Button(driver, (By.XPATH, '//*[@id="closeLargeModal"]'))
        self.body_large_modal = TextField(driver, (By.XPATH, '//*[@class="modal-body"]'))
        self.title_large_modal = Title(driver, (By.XPATH, '//*[@id="example-modal-sizes-title-lg"]'))

    def check_modal_dialogs(self, key):
        if key == 'small':
            self.small_modal_btn.is_visible()
            self.small_modal_btn.click()
            self.title_small_modal.is_visible()
            title_small = self.title_small_modal.text()
            self.body_small_modal.is_visible()
            body_small = self.body_small_modal.text()
            self.small_modal_close_btn.is_visible()
            self.small_modal_close_btn.click()
            return [title_small, len(body_small)]
        elif key == 'large':
            self.large_modal_btn.is_visible()
            self.large_modal_btn.click()
            self.title_large_modal.is_visible()
            title_large = self.title_large_modal.text()
            self.body_large_modal.is_visible()
            body_large = self.body_large_modal.text()
            self.large_modal_close_bnt.is_visible()
            self.large_modal_close_bnt.click()
            return [title_large, len(body_large)]
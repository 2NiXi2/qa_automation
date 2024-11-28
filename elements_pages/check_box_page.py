import random
import time

from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.button import Button
from locators.elements_page_locators import CheckBoxPageLocators
from pages.base_page import BasePage


class CheckPage(BasePage):
    locators = CheckBoxPageLocators

    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/checkbox')
        self.expand_all = Button(driver, (By.XPATH, "//button[@title='Expand all']"))
        self.item_list = BaseElement(driver, (By.XPATH, "//span[@class='rct-title']"))
        self.checked_items = BaseElement(driver, (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']"))
        self.output_result = BaseElement(driver, (By.XPATH, '//span[@class="text-success"]'))

    def open_full_list(self):
        self.expand_all.is_visible.click()

    def click_random_checkbox(self):
        item_list = self.item_list.are_visible()
        cnt = 21
        while cnt != 0:
            item = item_list[random.randint(1, 15)]
            if cnt > 0:
                self.go_to_element(item)
                item.click()
                cnt -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.checked_items.are_present()
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', ".//ancestor::span[@class='rct-text']")
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.output_result.are_present()
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()

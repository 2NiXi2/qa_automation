import base64
import os
import time
import random

import allure
import requests

from selenium.webdriver.common.by import By

from elements.button import Button
from elements.text_field import TextField
from generator.generator import generated_person
from pages.base_page import BasePage


class TextBoxPersonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/text-box')
        self.full_name_field = TextField(driver, (By.XPATH, '//*[@id="userName"]'))
        self.email_field = TextField(driver, (By.XPATH, '//*[@id="userEmail"]'))
        self.current_address_field = TextField(driver, (By.XPATH, '//*[@id="currentAddress"]'))
        self.permanent_address_field = TextField(driver, (By.XPATH, '//*[@id="permanentAddress"]'))
        self.submit_button = Button(driver, (By.XPATH, '//*[@id="submit"]'))

        self.created_full_name = TextField(driver, (By.XPATH, '//*[@id="name"]'))
        self.created_email = TextField(driver, (By.XPATH, '//*[@id="email"]'))
        self.created_current_address = TextField(driver, (By.XPATH, '//*[@id="currentAddress" and @class="mb-1"]'))
        self.created_permanent_address = TextField(driver, (By.XPATH, '//*[@id="permanentAddress" and @class="mb-1"]'))

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.full_name_field.type(full_name)
        self.email_field.type(email)
        self.current_address_field.type(current_address)
        self.permanent_address_field.type(permanent_address)
        self.submit_button.scroll_into_view().click()
        return full_name, email, current_address, permanent_address

    def check_fields(self):
        full_name = self.created_full_name.text().split(':')[1]
        email = self.created_email.text().split(':')[1]
        current_address = self.created_current_address.text().split(':')[1]
        permanent_address = self.created_permanent_address.text().split(':')[1]
        return full_name, email, current_address, permanent_address

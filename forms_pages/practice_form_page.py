import os
import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.check_box import CheckBox
from elements.date_picker import DatePicker
from elements.pop_up import PopUp
from elements.radio_button import RadioButton
from elements.text_field import TextField
from generator.generator import generated_person, generated_file, generated_subject
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/automation-practice-form')
        self.first_name = TextField(driver, (By.XPATH, '//*[@id="firstName"]'))
        self.last_name = TextField(driver, (By.XPATH, '//*[@id="lastName"]'))
        self.email = TextField(driver, (By.XPATH, '//*[@id="userEmail"]'))
        self.gender = RadioButton(driver, (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']"))
        self.mobile = TextField(driver, (By.XPATH, '//*[@id="userNumber"]'))
        self.date_of_birth = DatePicker(driver, (By.XPATH, '//*[@id="dateOfBirthInput"]'))
        self.subject = TextField(driver, (By.XPATH, '//*[@id="subjectsInput"]'))
        self.hobbies = CheckBox(driver, (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]'))
        self.file_input = Button(driver, (By.XPATH, '//*[@id="uploadPicture"]'))
        self.current_address = TextField(driver, (By.XPATH, '//*[@id="currentAddress"]'))
        self.select_state = Button(driver, (By.XPATH, '//*[@id="state"]'))
        self.state_input = TextField(driver, (By.XPATH, '//*[@id="react-select-3-input"]'))
        self.select_city = Button(driver, (By.XPATH, '//*[@id="city"]'))
        self.city_input = TextField(driver, (By.XPATH, '//*[@id="react-select-4-input"]'))
        self.submit = Button(driver, (By.XPATH, '//*[@id="submit"]'))
        self.result_table = PopUp(driver, (By.XPATH, '/html/body/div[5]/div/div/div[2]/div/table/tbody/tr[1]/td[2]'))

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subjects = generated_subject()
        self.first_name.is_visible()
        self.first_name.type(person.first_name)
        self.last_name.is_visible()
        self.last_name.type(person.last_name)
        self.email.is_visible()
        self.email.type(person.email)
        self.gender.is_visible()
        self.gender.click()
        self.mobile.is_visible()
        self.mobile.type(person.mobile)
        self.subject.is_visible()
        self.subject.scroll_into_view()
        self.subject.type(subjects)
        self.subject.send_keys(Keys.RETURN)
        self.hobbies.is_visible()
        self.hobbies.click()
        self.file_input.is_present()
        self.file_input.send_keys(path)
        os.remove(path)
        self.current_address.is_visible()
        self.current_address.type(person.current_address)
        self.select_state.is_visible()
        self.select_state.click()
        self.state_input.type(Keys.RETURN)
        self.select_city.is_visible()
        self.select_city.click()
        self.city_input.send_keys(Keys.RETURN)
        self.submit.is_present()
        self.submit.click()
        return person

    def form_result(self):
        result_list = self.result_table.are_present()
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
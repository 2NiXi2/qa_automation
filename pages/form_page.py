import os

import allure
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file, generated_subject
from locators.form_page_locatros import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    locators = FormPageLocators

    @allure.step('Fill in all fields')
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subjects = generated_subject()
        with allure.step('Filing fields'):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
            self.element_is_visible(self.locators.GENDER).click()
            self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
            subject = self.element_is_visible(self.locators.SUBJECT)
            subject.send_keys(subjects)
            subject.send_keys(Keys.RETURN)
            self.go_to_element(subject)
            self.element_is_visible(self.locators.HOBBIES).click()
        with allure.step('Fill path'):
            self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        with allure.step('Delete path'):
            os.remove(path)
        with allure.step('Fill other fields'):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
            self.element_is_visible(self.locators.SELECT_STATE).click()
            self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
            self.element_is_visible(self.locators.SELECT_CITY).click()
            self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        with allure.step('Click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return person

    @allure.step('Get form result')
    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data

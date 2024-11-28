from selenium.webdriver.common.by import By

from elements.base_element import BaseElement
from elements.button import Button
from elements.list import List
from elements.pop_up import PopUp
from elements.text_field import TextField
from generator.generator import generated_person
from pages.base_page import BasePage


class WebTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/webtables')
        #add person form
        self.add = Button(driver, (By.CSS_SELECTOR, '#addNewRecordButton'))
        self.firstname = TextField(driver, (By.XPATH, '//*[@id="firstName"]'))
        self.lastname = TextField(driver, (By.XPATH, '//*[@id="lastName"]'))
        self.email = TextField(driver, (By.XPATH, '//*[@id="userEmail"]'))
        self.age = TextField(driver, (By.XPATH, '//*[@id="age"]'))
        self.salary = TextField(driver, (By.XPATH, '//*[@id="salary"]'))
        self.department = TextField(driver, (By.XPATH, '//*[@id="department"]'))
        self.submit = Button(driver, (By.XPATH, '//*[@id="submit"]'))

        #tables
        self.full_people = List(driver, (By.XPATH, '//*[@class="rt-tr-group"]'))
        self.search = TextField(driver, (By.XPATH, '//*[@id="searchBox"]'))
        self.delete = Button(driver, (By.XPATH, '//*[@title="Delete"]'))
        self.no_rows_found = PopUp(driver, (By.XPATH, '//*[@class="rt-noData"]'))
        self.count_row = List(driver, (By.CSS_SELECTOR, 'select[aria-label="rows per page"'))
        self.count_row_btn = Button(driver, (By.CSS_SELECTOR, 'select[aria-label="rows per page"'))


        #update
        self.update = Button(driver, (By.XPATH, '//*[@title="Edit"]'))

    def add_new_person(self):
        cnt = 1
        while cnt != 0:
            person_info = next(generated_person())
            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.add.is_visible()
            self.add.click()
            self.firstname.type(firstname)
            self.lastname.type(lastname)
            self.email.type(email)
            self.age.type(age)
            self.salary.type(salary)
            self.department.type(department)
            self.submit.click()
            cnt -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.full_people.are_present()
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.search.type(key_word)

    def check_search_person(self):
        delete_button = self.delete.is_present()
        row = delete_button.find_element('xpath', ".//ancestor::div[@class='rt-tr-group']")
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.update.click()
        self.age.is_visible()
        self.age.type(age)
        self.submit.is_visible()
        self.submit.click()
        return str(age)

    def delete_person(self):
        self.delete.is_visible()
        self.delete.click()

    def check_deleted(self):
        self.no_rows_found.is_present()
        return self.no_rows_found.text()

    def select_up_to_some_rows(self):
        cnt = [5, 10, 20, 25, 50, 100]
        data = []
        for x in cnt:
            self.count_row_btn.scroll_into_view().click()
            self.driver.find_element(By.CSS_SELECTOR, f'option[value="{x}"]').click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        return len(self.full_people.are_present)
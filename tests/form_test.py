import time

import allure

from pages.form_page import FormPage
from conftest import driver


@allure.suite('Forms')
class TestForm:
    @allure.feature('FormPage')
    class TestFormPage:
        @allure.title('Check form')
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [person.first_name + ' ' + person.last_name, person.email] == [result[0], result[
                1]], 'the form has not been filled'

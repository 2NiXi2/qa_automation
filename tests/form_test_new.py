from forms_pages.practice_form_page import PracticeFormPage
from conftest import driver


class TestFormPage:
    def test_form(self, driver):
        form_page = PracticeFormPage(driver)
        form_page.open()
        person = form_page.fill_form_fields()
        result = form_page.form_result()
        print(person, result, sep='\n')
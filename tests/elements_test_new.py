import allure
import random
import time

from elements_pages.buttons_page import ButtonsPage
from elements_pages.check_box_page import CheckPage

from conftest import driver
from elements_pages.dynamic_properties_page import DynamicPropertiesPage
from elements_pages.links_page import LinksPage
from elements_pages.radio_button_page import RadioButtonPageCheck
from elements_pages.text_box_page import TextBoxPersonPage
from elements_pages.upload_and_download_page import UploadAndDownloadPage
from elements_pages.web_table_page import WebTablePage


class TestTable:
    def test_table_fields(self, driver):
        fields_page = TextBoxPersonPage(driver)
        fields_page.open()
        full_name, email, current_address, permanent_address = fields_page.fill_all_fields()
        full_name_cr, email_cr, current_address_cr, permanent_address_cr = fields_page.check_fields()
        print(full_name, email, current_address, permanent_address)
        print(full_name_cr, email_cr, current_address_cr, permanent_address_cr)
        assert full_name == full_name_cr
        assert email == email_cr
        assert current_address == current_address_cr
        assert permanent_address == permanent_address_cr


class TestCheckPage:
    def test_check_page(self, driver):
        check_page = CheckPage(driver)
        check_page.open()
        check_page.open_full_list()
        check_page.click_random_checkbox()
        check = check_page.get_checked_checkboxes()
        output = check_page.get_output_result()
        assert check == output


class TestRadioButtonPageCheck:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPageCheck(driver)
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        yes_out = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        impressive_out = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        no_out = radio_button_page.get_output_result()
        assert yes_out == 'Yes'
        assert impressive_out == 'Impressive'
        assert no_out == 'No'


class TestWebTable1:

    @allure.title('Check to add a person to the table')
    def test_web_table_add(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        added_person = web_table_page.check_new_added_person()
        print(new_person, added_person, sep='\n')
        assert new_person in added_person

    @allure.title('Check human search in table')
    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        time.sleep(0.5)
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        print(key_word, table_result, sep='\n')
        assert key_word in table_result

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()
        last_name = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(last_name)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        print(last_name, age, row, sep='\n')
        assert age in row

    def test_web_table_delete_person_info(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == 'No rows found'

    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver)
        web_table_page.open()
        cnt = web_table_page.select_up_to_some_rows()
        avg = web_table_page.check_count_rows()
        print(cnt, avg, sep='\n')
        assert cnt == [5, 10, 20, 25, 50,
                       100], 'The number of rows in the table has not been changed or has changed incorrectly'
        assert avg == 100, 'Count rows not 100'

        #https://vk.com/video-197934479_456239240


class TestButtonsPage:
    def test_different_click_on_the_button(self, driver):
        buttons_page = ButtonsPage(driver)
        buttons_page.open()
        double = buttons_page.click_on_different_button('double')
        right = buttons_page.click_on_different_button('right')
        dynamic = buttons_page.click_on_different_button('dynamic')
        assert double == 'You have done a double click'
        assert right == 'You have done a right click'
        assert dynamic == 'You have done a dynamic click'


class TestLinksPage:
    def test_check_link(self, driver):
        links_page = LinksPage(driver)
        links_page.open()
        href_link, crt_link = links_page.check_new_tab_simple_link()
        assert href_link == crt_link

    def test_broken_link(self, driver):
        links_page = LinksPage(driver)
        links_page.open()
        res_code = links_page.check_broken_link('https://demoqa.com/bad-request')
        assert res_code == 400


class TestUploadAndDownload:
    def test_upload_file(self, driver):
        upload_file_page = UploadAndDownloadPage(driver)
        upload_file_page.open()
        file_name, result = upload_file_page.upload_file()
        assert file_name == result

    def test_download_file(self, driver):
        upload_download_page = UploadAndDownloadPage(driver)
        upload_download_page.open()
        check = upload_download_page.download_file()
        assert check is True, "the file has not been downloaded"


class TestDynamicProperties:
    def test_enable_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable == True

    def test_dynamic_properties(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_before != color_after

    def test_appear_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver)
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_button()
        assert appear is True, 'button did not appear after 5 seconds'

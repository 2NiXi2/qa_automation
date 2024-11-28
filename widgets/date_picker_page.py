import random

from selenium.webdriver.common.by import By

from elements.list import List
from elements.selector import Selector
from elements.text_field import TextField
from generator.generator import generated_date
from pages.base_page import BasePage

from selenium.webdriver.support.select import Select


class DatePickerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/date-picker')
        #date
        self.date_input = TextField(driver, (By.XPATH, '//*[@id="datePickerMonthYearInput"]'))
        self.date_select_month = Selector(driver, (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]'))
        self.date_select_year = Selector(driver, (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]'))
        self.date_select_day_list = List(driver, (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]'))
        #date and time
        self.date_and_time_input = TextField(driver, (By.XPATH, '//*[@id="dateAndTimePickerInput"]'))
        self.date_and_time_month = Selector(driver, (By.XPATH, '//*[@class="react-datepicker__month-read-view"]'))
        self.date_and_time_year = Selector(driver, (By.XPATH, '//*[@class="react-datepicker__year-read-view"]'))
        self.date_and_time_time_list = List(driver, (By.XPATH, '//*[@class="react-datepicker__time-list-item "]'))
        self.date_and_time_month_list = List(driver, (By.XPATH, '//*[@class="react-datepicker__month-option"]'))
        self.date_and_time_year_list = List(driver, (By.XPATH, '//*[@class="react-datepicker__year-option"]'))

    def select_date(self):
        date = next(generated_date())
        input_date = self.date_input.is_visible()
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.date_select_month, date.month)
        self.set_date_by_text(self.date_select_year, date.year)
        self.set_date_item_from_list(self.date_select_day_list, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.date_and_time_input.is_visible()
        self.date_and_time_input.scroll_into_view()
        value_date_before = input_date.get_attribute('value')
        self.date_and_time_input.click()
        self.date_and_time_month.is_clickable()
        self.date_and_time_month.click()
        self.set_date_item_from_list(self.date_and_time_month_list, date.month)
        self.date_and_time_year.is_clickable()
        self.date_and_time_year.click()
        self.set_date_item_from_list(self.date_and_time_year_list, str(random.randint(2020, 2028)))
        self.set_date_item_from_list(self.date_select_day_list, date.day)
        self.set_date_item_from_list(self.date_and_time_time_list, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(element.is_present())
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = elements.are_visible()
        for item in item_list:
            if item.text == value:
                item.click()
                break
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from elements.text_field import TextField
from elements.title import Title
from pages.base_page import BasePage


class AccordianPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/accordian')
        #section1
        self.section_first = Title(driver, (By.XPATH, '//*[@id="section1Heading"]'))
        self.section_first_content = TextField(driver, (By.XPATH, '//*[@id="section1Content"]/p'))
        #section2
        self.section_second = Title(driver, (By.XPATH, '//*[@id="section2Heading"]'))
        self.section_second_content = TextField(driver, (By.XPATH, '//*[@id="section2Content"]'))
        #section3
        self.section_third = Title(driver, (By.XPATH, '//*[@id="section3Heading"]'))
        self.section_third_content = TextField(driver, (By.XPATH, '//*[@id="section3Content"]/p'))

    def check_accordian(self, ac_num):
        accordian = {
            'first':
                {'title': self.section_first,
                 'content': self.section_first_content},
            'second':
                {'title': self.section_second,
                 'content': self.section_second_content},
            'third':
                {'title': self.section_third,
                 'content': self.section_third_content}
        }

        accordian[ac_num]['title'].is_present()
        accordian[ac_num]['title'].scroll_into_view()
        accordian[ac_num]['title'].click()
        section_title = accordian[ac_num]['title'].text()
        try:
            accordian[ac_num]['content'].is_visible()
            section_content = accordian[ac_num]['content'].text()
        except TimeoutException:
            accordian[ac_num]['title'].click()
            accordian[ac_num]['content'].is_visble()
            section_content = accordian[ac_num]['content'].text()
        return [section_title, len(section_content)]
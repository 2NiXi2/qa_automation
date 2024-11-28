import requests
from selenium.webdriver.common.by import By

from elements.link import Link
from pages.base_page import BasePage


class LinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/links')
        self.simple_link = Link(driver, (By.XPATH, '//*[@id="simpleLink"]'))
        self.bad_request = Link(driver, (By.XPATH, '//*[@id="bad-request"]'))

    def check_new_tab_simple_link(self):
        self.simple_link.is_visible()
        link_href = self.simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            self.simple_link.click()
            self.switch_tab(1)
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.bad_request.click()
        else:
            return request.status_code
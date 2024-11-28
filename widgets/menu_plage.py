from selenium.webdriver.common.by import By

from elements.list import List
from pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.menu_item_list = List(driver, (By.CSS_SELECTOR, 'ul[id="nav"] li a'))

    def check_menu(self):
        menu = self.menu_item_list.are_present()
        data = []
        for item in menu:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
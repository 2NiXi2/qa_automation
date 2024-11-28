import random

from selenium.webdriver.common.by import By

from elements.list import List
from elements.tab import Tab
from pages.base_page import BasePage


class SelectablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.tab_list = Tab(driver, (By.XPATH, '//*[@id="demo-tab-list"]'))
        self.list_item = Tab(driver, (By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']"))
        self.list_item_active = Tab(driver, (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]'))
        self.tab_grid = Tab(driver, (By.XPATH, '//*[@id="demo-tab-grid"]'))
        self.grid_item = Tab(driver,
        (By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]'))
        self.grid_item_active = Tab(driver,
        (By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]'))

    def click_selectable_item(self, elements, cnt):
        item_list = elements.are_visible()
        selected_items = random.sample(item_list, k=random.randint(1, cnt))
        for item in selected_items:
            self.go_to_element(item)
            item.click()

    def select_list_item(self):
        self.tab_list.is_visible()
        self.tab_list.click()
        self.click_selectable_item(self.list_item, 4)
        active_item = self.list_item_active.is_visible()
        return active_item.text

    def select_grid_item(self):
        self.tab_grid.is_visible()
        self.tab_grid.click()
        self.click_selectable_item(self.grid_item, 8)
        active_element = self.grid_item_active.is_visible()
        return active_element.text
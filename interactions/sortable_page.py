import random

from selenium.webdriver.common.by import By

from elements.list import List
from elements.tab import Tab
from pages.base_page import BasePage


class SortablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.tab_list = Tab(driver, (By.XPATH, '//*[@id="demo-tab-list"]'))
        self.list_item = List(driver, (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]'))
        self.tab_grid = Tab(driver, (By.XPATH, '//*[@id="demo-tab-grid"]'))
        self.grid_item = List(driver, (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]'))

    def get_sortable_items(self, elements):
        item_list = elements.are_visible()
        return [item.text for item in item_list]

    def change_list_order(self):
        self.tab_list.is_visible()
        self.tab_list.click()
        order_before = self.get_sortable_items(self.list_item)
        item_list = random.sample(self.list_item.are_visible(), k=2)
        item_what = item_list[0]
        self.go_to_element(item_what)
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.list_item)
        return order_before, order_after

    def change_grid_order(self):
        self.tab_grid.is_visible()
        self.tab_grid.click()
        order_before = self.get_sortable_items(self.grid_item)
        item_list = random.sample(self.grid_item.are_visible(), k=2)
        item_what = item_list[0]
        self.go_to_element(item_what)
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.grid_item)
        return order_before, order_after
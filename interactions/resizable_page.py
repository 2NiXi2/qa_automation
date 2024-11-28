import time
import random

from selenium.webdriver.common.by import By

from elements.tab import Tab
from pages.base_page import BasePage


class ResizablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.resizable_box_handle = Tab(driver, (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]'))
        self.resizable_box = Tab(driver, (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]'))
        self.resizable_handle = Tab(driver, (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]'))
        self.resizable = Tab(driver, (By.CSS_SELECTOR, 'div[id="resizable"]'))
        self.resizable_title = Tab(driver, (By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[1]'))
        self.resizable_title_handle = Tab(driver, (By.CSS_SELECTOR, '//*[@id="resizable"]/div'))

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = element.is_visible()
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.resizable_title.is_visible()
        self.resizable_title.scroll_into_view()
        self.action_drag_and_drop_by_offset(self.resizable_box_handle.is_present(), 400, 200)
        time.sleep(0.5)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.resizable_box))
        self.action_drag_and_drop_by_offset(self.resizable_box_handle.is_present(), -350, -150)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.resizable_box))
        return max_size, min_size

    def change_size_resizable(self):
        self.resizable_handle.is_visible()
        self.resizable_handle.scroll_into_view()
        self.action_drag_and_drop_by_offset(self.resizable_handle.is_visible(),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.resizable))
        self.action_drag_and_drop_by_offset(self.resizable_handle.is_visible(),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.resizable))
        return max_size, min_size

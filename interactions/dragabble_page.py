import allure
import random
import re
from selenium.webdriver.common.by import By

from elements.tab import Tab
from pages.base_page import BasePage


class DragabblePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        # Simple
        self.simple_tab = Tab(driver, (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]'))
        self.drag_me = Tab(driver, (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]'))
        # Axis Restricted
        self.axis_tab = Tab(driver, (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]'))
        self.only_x = Tab(driver, (By.CSS_SELECTOR, 'div[id="restrictedX"]'))
        self.only_y = Tab(driver, (By.CSS_SELECTOR, 'div[id="restrictedY"]'))

    @allure.step('Get before and after positions')
    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step('Simple drag and drop')
    def simple_drag_box(self):
        self.simple_tab.is_visible()
        self.simple_tab.click()
        drag_div = self.drag_me.is_visible()
        before_position, after_position = self.get_before_and_after_position(drag_div)
        return before_position, after_position

    @allure.step('Get top position')
    def get_top_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[2])

    @allure.step('Get left position')
    def get_left_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[1])

    @allure.step('Drag only_x')
    def axis_restricted_x(self):
        self.axis_tab.is_visible()
        self.axis_tab.scroll_into_view().click()
        only_x = self.only_x.is_visible()
        position_x = self.get_before_and_after_position(only_x)
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    @allure.step('Drag only_y')
    def axis_restricted_y(self):
        self.axis_tab.is_visible()
        self.axis_tab.scroll_into_view().click()
        only_y = self.only_y.is_visible()
        position_x = self.get_before_and_after_position(only_y)
        top_y_before = self.get_top_position(position_x[0])
        top_y_after = self.get_top_position(position_x[1])
        left_y_before = self.get_left_position(position_x[0])
        left_y_after = self.get_left_position(position_x[1])
        return [top_y_before, top_y_after], [left_y_before, left_y_after]
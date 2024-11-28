from selenium.webdriver.common.by import By
import time

from elements.tab import Tab
from pages.base_page import BasePage


class DroppablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        # Simple
        self.simple_tab = Tab(driver, (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']"))
        self.drag_me_simple = Tab(driver, (By.CSS_SELECTOR, 'div[id="draggable"]'))
        self.drop_here_simple = Tab(driver, (By.CSS_SELECTOR, '#simpleDropContainer #droppable'))
        # Accept
        self.accept_tab = Tab(driver, (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']"))
        self.acceptable = Tab(driver, (By.CSS_SELECTOR, 'div[id="acceptable"]'))
        self.not_acceptable = Tab(driver, (By.CSS_SELECTOR, 'div[id="notAcceptable"]'))
        self.drop_here_accept = Tab(driver, (By.CSS_SELECTOR, '#acceptDropContainer #droppable'))
        # Prevent Propogation
        self.prevent_tab = Tab(driver, (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']"))
        self.not_greedy_drop_box_text = Tab(driver, (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)'))
        self.not_greedy_inner_box = Tab(driver, (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]'))
        self.greedy_drop_box_text = Tab(driver, (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)'))
        self.greedy_inner_box = Tab(driver, (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]'))
        self.drag_me_prevent = Tab(driver, (By.CSS_SELECTOR, '#ppDropContainer #dragBox'))
        # Revert Draggable
        self.revert_tab = Tab(driver, (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']"))
        self.will_revert = Tab(driver, (By.CSS_SELECTOR, 'div[id="revertable"]'))
        self.not_revert = Tab(driver, (By.CSS_SELECTOR, 'div[id="notRevertable"]'))
        self.drop_here_revert = Tab(driver, (By.CSS_SELECTOR, '#revertableDropContainer #droppable'))

    def drop_simple(self):
        self.simple_tab.is_visible()
        self.simple_tab.scroll_into_view().click()
        #self.simple_tab.click()
        drag_div = self.drag_me_simple.is_visible()
        drop_div = self.drop_here_simple.is_visible()
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.accept_tab.is_visible()
        self.accept_tab.scroll_into_view().click()
        #self.accept_tab.click()
        acceptable_div = self.acceptable.is_visible()
        not_acceptable_div = self.not_acceptable.is_visible()
        drop_div = self.drop_here_accept.is_visible()
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_not_accept, drop_text_accept

    def drop_prevent_propogation(self):
        self.prevent_tab.is_visible()
        self.prevent_tab.scroll_into_view().click()
        drag_div = self.drag_me_prevent.is_visible()
        not_greedy_inner_box = self.not_greedy_inner_box.is_visible()
        greedy_inner_box = self.greedy_inner_box.is_visible()
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        self.not_greedy_drop_box_text.is_visible()
        text_not_greedy_box = self.not_greedy_drop_box_text.text()
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        self.greedy_drop_box_text.is_visible()
        text_greedy_box = self.greedy_drop_box_text.text()
        text_greedy_inner_box = greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revert_draggable(self, type_drag):
        drags = {
            'will':
                {'revert': self.will_revert, },
            'not_will':
                {'revert': self.not_revert},
        }
        self.revert_tab.is_visible()
        self.revert_tab.click()
        revert = drags[type_drag]['revert'].is_visible()
        drop_div = self.drop_here_revert.is_visible()
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert
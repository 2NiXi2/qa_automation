import allure
from selenium.webdriver.common.by import By

from elements.tab import Tab
from elements.text_field import TextField
from pages.base_page import BasePage


class TabsPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.tabs_what = Tab(driver, (By.CSS_SELECTOR, 'a[id="demo-tab-what"]'))
        self.tabs_what_content = TextField(driver, (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]'))
        self.tabs_what_origin = Tab(driver, (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]'))
        self.tabs_what_origin_content = TextField(driver, (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]'))
        self.tabs_use = Tab(driver, (By.CSS_SELECTOR, 'a[id="demo-tab-use"]'))
        self.tabs_use_content = TextField(driver,(By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]'))
        self.tabs_more = Tab(driver, (By.CSS_SELECTOR, 'a[id="demo-tab-more"]'))
        self.tabs_more_content = TextField(driver, (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]'))

    def check_tabs(self, tab):
        with allure.step('Fill tabs'):
            tabs = {'what':
                        {'title': self.tabs_what,
                         'content': self.tabs_what_content},
                    'origin':
                        {'title': self.tabs_what_origin,
                         'content': self.tabs_what_origin_content},
                    'use':
                        {'title': self.tabs_use,
                         'content': self.tabs_use_content},
                    'more':
                        {'title': self.tabs_more,
                         'content': self.tabs_more_content},
                    }
        with allure.step('Click button'):
            tabs[tab]['title'].is_visible()
            tabs[tab]['title'].scroll_into_view()
            tabs[tab]['title'].click()
            tabs[tab]['content'].is_visible()
            what_content = tabs[tab]['content'].text()
        return tabs[tab]['title'].text(), len(what_content)
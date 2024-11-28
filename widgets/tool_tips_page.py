from selenium.webdriver.common.by import By
import time

from elements.button import Button
from elements.text_field import TextField
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.tool_btn = Button(driver, (By.XPATH, '//*[@id="toolTipButton"]'))
        self.tool_btn_area = TextField(driver, (By.XPATH, '//*[@id="buttonToolTip"]/div[2]'))

        self.field = TextField(driver, (By.CSS_SELECTOR, 'input[id="toolTipTextField"]'))
        self.tool_field = TextField(driver, (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]'))

        self.contrary_link = TextField(driver, (By.XPATH, '//*[.="Contrary"]'))
        self.tool_contrary = TextField(driver, (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]'))

        self.sectional_link = TextField(driver, (By.XPATH, '//*[.="1.10.32"]'))
        self.tool_sectional = TextField(driver, (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]'))

        self.tool_inners = TextField(driver, (By.CSS_SELECTOR, 'div[class="tooltip-inner"]'))

    def get_text_from_tool_tips(self, hov_elm, wait_elm):
        element = hov_elm.is_present()
        self.action_move_to_element(element)
        time.sleep(0.5)
        wait_elm.is_visible()
        self.tool_inners.is_visible()
        self.tool_inners.scroll_into_view()
        text = self.tool_inners.text()
        time.sleep(0.5)
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.tool_btn, self.tool_btn_area)
        tool_tip_text_field = self.get_text_from_tool_tips(self.field, self.tool_field)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.contrary_link,
                                                              self.tool_contrary)
        tool_tip_text_section = self.get_text_from_tool_tips(self.sectional_link, self.tool_sectional)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
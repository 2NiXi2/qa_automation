import allure
from elements.base_element import BaseElement
from selenium.webdriver import ActionChains as AC


class Button(BaseElement):

    @allure.step('Double click')
    def action_double_click(self):
        action = AC(self.driver)
        action.double_click(self.find())
        action.perform()

    @allure.step('Right click')
    def action_right_click(self):
        action = AC(self.driver)
        action.context_click(self.find())
        action.perform()

    def get_attribute(self, value):
        element = self.find_element()
        return element.get_attribute(value)
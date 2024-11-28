import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, driver, locator, timeout=5):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.wait = wait(driver, timeout)

    def find(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            raise Exception(f"Элемент с локатором {self.locator} не найден.")

    def find_element(self):
        by, value = self.locator
        element = self.driver.find_element(by, value)
        return element

    #@property
    @allure.step('Find a visible element')
    def is_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find visible elements')
    def are_visible(self):
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find a present element')
    def is_present(self):
        try:
            return self.wait.until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find present elements')
    def are_present(self):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(self.locator))
        except TimeoutException:
            return False

    @property
    def is_not_visible(self):
        try:
            return self.wait.until(EC.invisibility_of_element_located(self.locator))
        except TimeoutException:
            return False

    @allure.step('Find clickable elements')
    def is_clickable(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.locator))
        except TimeoutException:
            return False

    def click(self):
        element = self.find_element()
        element.click()

    def text(self):
        element = self.find_element()
        return element.text

    def send_keys(self, value):
        element = self.find_element()
        element.send_keys(value)
    def scroll_into_view(self):
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def value_of_css_property(self, value):
        element = self.find_element()
        return element.value_of_css_property(value)
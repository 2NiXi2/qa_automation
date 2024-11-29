import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, Union


class BaseElement:
    def __init__(self, driver: WebDriver, locator: Tuple[str, str], timeout: int = 5):
        self.driver: WebDriver = driver
        self.locator: Tuple[str, str] = locator
        self.timeout: int = timeout
        self.wait = wait(driver, timeout)

    def find(self) -> WebElement:
        try:
            return self.wait.until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            raise Exception(f"Элемент с локатором {self.locator} не найден.")

    def find_element(self) -> WebElement:
        by, value = self.locator
        element = self.driver.find_element(by, value)
        return element

    #@property
    @allure.step('Find a visible element')
    def is_visible(self) -> Union[WebElement, bool]:
        try:
            return self.wait.until(EC.visibility_of_element_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find visible elements')
    def are_visible(self) -> Union[list, bool]:
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find a present element')
    def is_present(self) -> Union[WebElement, bool]:
        try:
            return self.wait.until(EC.presence_of_element_located(self.locator))
        except TimeoutException:
            return False

    #@property
    @allure.step('Find present elements')
    def are_present(self) -> Union[list, bool]:
        try:
            return self.wait.until(EC.presence_of_all_elements_located(self.locator))
        except TimeoutException:
            return False

    @property
    def is_not_visible(self) -> Union[WebElement, bool]:
        try:
            return self.wait.until(EC.invisibility_of_element_located(self.locator))
        except TimeoutException:
            return False

    @allure.step('Find clickable elements')
    def is_clickable(self) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable(self.locator))
            return True
        except TimeoutException:
            return False

    def click(self) -> None:
        element = self.find_element()
        element.click()

    def text(self) -> str:
        element = self.find_element()
        return element.text

    def send_keys(self, value: str):
        element = self.find_element()
        element.send_keys(value)
    def scroll_into_view(self) -> WebElement:
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def value_of_css_property(self, value: str):
        element = self.find_element()
        return element.value_of_css_property(value)
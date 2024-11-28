import allure

from alerts_frame_and_windows.alerts_page import AlertsPage
from alerts_frame_and_windows.frames_page import FramesPage
from alerts_frame_and_windows.modal_dialogs_page import ModalDialogsPage
from alerts_frame_and_windows.nested_frames_page import NestedFramesPage
from conftest import driver
from alerts_frame_and_windows.browser_windows_page import BrowserWindowsPage


class TestBrowserWindowsPage:
    def test_new_tab(self, driver):
        browser_page = BrowserWindowsPage(driver)
        browser_page.open()
        tab = browser_page.check_frame('tab')
        window = browser_page.check_frame('window')
        assert tab == 'This is a sample page'
        assert window == 'This is a sample page'

class TestAlertsPage:
    def test_see_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open()
        alert = alerts_page.check_see_alert()
        assert alert == 'You clicked a button', 'Alert did not show up'

    @allure.title('Checking the opening of the alert after 5 seconds')
    def test_alert_appear_5_sec(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open()
        alert = alerts_page.check_alert_appear_5_sec()
        assert alert == 'This alert appeared after 5 seconds', 'Alert did not show up'

    @allure.title('Checking the opening of the alert with confirm')
    def test_confirm_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open()
        alert_text = alerts_page.check_confirm_alert()
        assert alert_text == 'You selected Ok', "Alert did not show up"

    @allure.title('Checking the opening of the alert with prompt')
    def test_prompt_alert(self, driver):
        alerts_page = AlertsPage(driver)
        alerts_page.open()
        alert, text = alerts_page.check_prompt_alert()
        assert text in alert, "Alert did not show up"

class TestFramesPage:
    @allure.title('Check the page with frames')
    def test_frames(self, driver):
        frames_page = FramesPage(driver)
        frames_page.open()
        result_fr1 = frames_page.check_frame('frame1')
        result_fr2 = frames_page.check_frame('frame2')
        assert result_fr1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
        assert result_fr2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

class TestNestedFramesPage:
    def test_nested_frames(self, driver):
        nested_frame_page = NestedFramesPage(driver)
        nested_frame_page.open()
        parent_text, child_text = nested_frame_page.check_nested_frames()
        assert parent_text == 'Parent frame', 'Nested frame does not exist'
        assert child_text == 'Child Iframe', 'Nested frame does not exist'

class TestModalDialogsPage:
    def test_modal_dialogs(self, driver):
        modal_dialogs_page = ModalDialogsPage(driver)
        modal_dialogs_page.open()
        small = modal_dialogs_page.check_modal_dialogs('small')
        large = modal_dialogs_page.check_modal_dialogs('large')
        assert small[1] < large[1], 'text from large dialog is less than text from small dialog'
        assert small[0] == 'Small Modal', 'The header is not "Small modal"'
        assert large[0] == 'Large Modal', 'The header is not "Large modal"'
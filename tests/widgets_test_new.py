import allure


from widgets.accordian_page import AccordianPage
from conftest import driver
from widgets.auto_complete import AutoCompletePage
from widgets.date_picker_page import DatePickerPage
from widgets.menu_plage import MenuPage
from widgets.progress_bar_page import ProgressBarPage
from widgets.slider_page import SliderPage
from widgets.tabs_page import TabsPage
from widgets.tool_tips_page import ToolTipsPage


class TestAccordianPage:
    def test_accordian(self, driver):
        accordian_page = AccordianPage(driver)
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
        assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
        assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

class TestAutoCompletePage:
    @allure.title('Check the autocomplete is filled')
    def test_auto_complete(self, driver):
        auto_complete_page = AutoCompletePage(driver)
        auto_complete_page.open()
        colors = auto_complete_page.fill_input_multi()
        colors_result = auto_complete_page.check_color_in_multi()
        assert colors == colors_result, 'The added colors are missing in the input'

    @allure.title('Check deletions from the multi autocomplete')
    def test_remove_value_from_multi(self, driver):
        auto_complete_page = AutoCompletePage(driver)
        auto_complete_page.open()
        auto_complete_page.fill_input_multi()
        cnt_colors = auto_complete_page.remove_value_from_multi()
        cnt_colors_result = auto_complete_page.check_color_in_multi()
        assert cnt_colors != cnt_colors_result, 'Value was not detected'

    @allure.title('Check deletions from the single autocomplete')
    def test_fill_single_autocomplete(self, driver):
        auto_complete_page = AutoCompletePage(driver)
        auto_complete_page.open()
        color = auto_complete_page.fill_input_single()
        color_result = auto_complete_page.check_color_in_single()
        assert color == color_result, 'The added colors are missing in the input'


class TestDatePickerPage:
    @allure.title('Check change date')
    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(driver)
        date_picker_page.open()
        date_before, date_after = date_picker_page.select_date()
        assert date_before != date_after, 'The date has not been change'

    @allure.title('Check change date and time')
    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver)
        date_picker_page.open()
        date_before, date_after = date_picker_page.select_date_and_time()
        assert date_before != date_after, 'The date and time have not been change'

class TestSliderPage:
    def test_slider(self, driver):
        slider_page = SliderPage(driver)
        slider_page.open()
        before, after = slider_page.change_slider_value()
        assert before != after, 'The slider value has not been changed'

class TestProgressBarPage:
    def test_progress(self, driver):
        progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
        progress_bar_page.open()
        before, after = progress_bar_page.change_progress_bar_value()
        assert before != after

class TestTabsPage:
    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs_page.open()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        more_button, more_content = tabs_page.check_tabs('more')
        assert what_button == 'What' and what_content != 0, 'The tab "what" was not pressed or the text is missing'
        assert origin_button == 'Origin' and origin_content != 0, 'The tab "origin" was not pressed or the text is missing'
        assert use_button == 'Use' and use_content != 0, 'The tab "use" was not pressed or the text is missing'
        assert more_button == 'More' and what_content != 0, 'The tab "more" was not pressed or the text is missing'

class TestToolTips:
    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        print(button_text, field_text, contrary_text, section_text)
        assert button_text == 'You hovered over the Button', 'Hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'Hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

class TestMenuPage:
    def test_menu(self, driver):
        menu_page = MenuPage(driver, 'https://demoqa.com/menu')
        menu_page.open()
        menu = menu_page.check_menu()
        assert menu == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                        'Sub Sub Item 2', 'Main Item 3'], "menu items do not exist or have not been selected"












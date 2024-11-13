import allure

from conftest import driver
from pages.Interaction_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Interactions')
class TestInteractions:
    @allure.feature('Sortable Page')
    class TestSortablePage:
        @allure.title('Check changed sortable list and grid')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    @allure.feature('Selectable Page')
    class TestSelectablePage:
        @allure.title('Check changed selectable list and grid')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'No elements were selected'
            assert len(item_grid) > 0, 'No elements were selected'

    @allure.feature('Resizable Page')
    class TestResizablePage:
        @allure.title('Check changed resizable boxes')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_b, min_b = resizable_page.change_size_resizable_box()
            max_s, min_s = resizable_page.change_size_resizable()
            assert max_b == ('500px', '300px'), "Maximum size not equal to '500px', '300px'"
            assert min_b == ('150px', '150px'), "Minimum size not equal to '150px', '150px'"
            assert max_s != min_s, 'Resizable has not been changed'

    @allure.feature('Droppable Page')
    class TestDroppablePage:
        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The elements have not been droppped'

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', 'The dropped element has been accepted'
            assert accept == 'Dropped!', 'The dropped element has not been accepted'

        @allure.title('Check prevent propogation droppable')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            print(not_greedy, not_greedy_inner, greedy, greedy_inner, sep='\n')
            assert not_greedy == 'Dropped!', 'The elements text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'The elements text has not been changed'
            assert greedy == 'Outer droppable', 'The elements text has been changed'
            assert greedy_inner == 'Dropped!', 'The elements text has not been changed'

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'the elements has not reverted'
            assert not_will_after_move == not_will_after_revert, 'the elements has  reverted'

    @allure.feature('Draggable Page')
    class TestDraggablePage:
        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "the position of the box has not been changed"

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"
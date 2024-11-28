from elements.base_element import BaseElement


class TextField(BaseElement):
    def type(self, value):
        element = self.find_element()
        element.clear()
        element.send_keys(value)
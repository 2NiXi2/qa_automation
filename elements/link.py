from elements.base_element import BaseElement


class Link(BaseElement):
    def get_attribute(self, value):
        element = self.find_element()
        return element.get_attribute(value)

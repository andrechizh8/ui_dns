import selene
from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import Keys
from selene import command
import os


class CheckBox:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_checkbox(self, value):
        self.element.element_by(have.text(value)).click()
        return self


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, value):
        self.element.send_keys(Keys.CONTROL, 'a').send_keys(value).press_enter()
        return self


class DropDown:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_dropdown(self, selector, value):
        self.element.click()
        browser.element(selector).type(value).press_enter()
        return self


class RadioButton:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_radio(self, value):
        self.element.element_by(have.text(value)).click()
        return self

from selene import command
import os
import tests
from selene.support.shared import browser


def path_to(selector, path):
    """Path to file"""
    browser.element(selector).send_keys(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), path)))


def scroll_to_element(selector):
    """Scroll to element"""
    browser.element(selector).perform(command.js.scroll_into_view).click()



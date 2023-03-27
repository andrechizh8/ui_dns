from selene.support.shared import browser
from model import app
import time


def get_cities_list():
    """Get text (cities) from list of elements"""
    app.given_opened()
    browser.driver.maximize_window()
    browser.element(".city-select__text_BTU").click()
    time.sleep(2)
    a = browser.all("//*[@class='city-bubble_IBz']/a").locate()
    texts = [i.text for i in a]
    return texts

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from model.utils import attach
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = os.getenv("BASE_URL")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 20

    yield
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def selenoid_config():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('SELENOID_LOGIN')}:{os.getenv('SELENOID_PASSWORD')}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield browser

    attach.add_html(browser)
    attach.add_screenshots(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

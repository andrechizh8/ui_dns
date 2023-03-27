from selene.support.shared import browser
from model.components.authorization import Authorization
from model.pages.profile_page import ProfilePage
from model.pages.main_page import MainPage
from model.pages.select_page import ProductSelectPage
from model.pages.feedback_page import FeedbackPage
import os
from dotenv import load_dotenv

load_dotenv()
auth = Authorization()
profile = ProfilePage()
main_page = MainPage()
select_product = ProductSelectPage()
feedback = FeedbackPage()


def given_opened():
    url = os.getenv("BASE_URL")
    browser.open(url)

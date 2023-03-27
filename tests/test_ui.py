import os
import pytest
from dotenv import load_dotenv
from model.data.users import current_user
from model import app
import allure
from allure_commons.types import Severity

load_dotenv()
current_email = os.getenv("EMAIL")
current_password = os.getenv("PASSWORD")


class TestUi:

    @pytest.mark.login
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('Login')
    @allure.severity(Severity.CRITICAL)
    def test_login(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Open authorization window"):
            app.auth.open_login_window()
            app.auth.select_enter_button()

        with allure.step("Fill email"):
            app.auth.fill_email_input(current_email)

        with allure.step("Fill password"):
            app.auth.fill_password_input(current_password)
        # THEN
        with allure.step("Check user`s authorization"):
            app.auth.open_user_cabinet()
            app.auth.check_log_in()

        with allure.step("Logout form profile"):
            app.auth.open_logout_window()
            app.auth.click_logout()

    @pytest.mark.profile
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('Profile')
    @allure.severity(Severity.CRITICAL)
    def test_change_profile_data(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Open authorization window"):
            app.auth.open_login_window()
            app.auth.select_enter_button()

        with allure.step("Fill authorization info"):
            app.auth.fill_email_input(current_email)
            app.auth.fill_password_input(current_password)

        with allure.step("Open profile settings"):
            app.auth.open_user_cabinet()
            app.profile.open_profile_settings()

        with allure.step("Change first name"):
            app.profile.fill_first_name(current_user.first_name)

        with allure.step("Change last name"):
            app.profile.fill_last_name(current_user.last_name)

        with allure.step("Change nickname"):
            app.profile.fill_nickname(current_user.nickname)

        with allure.step("Change date"):
            app.profile.fill_birthday(current_user.date)

        with allure.step("Set avatar"):
            app.profile.set_avatar(current_user.file)
        # THEN
        with allure.step("Check the correct change of user data"):
            app.profile.check_nickname_change()

    @pytest.mark.wishlist
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('Wishlist')
    @allure.severity(Severity.NORMAL)
    def test_add_product_to_wishlist(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Search product to buy"):
            app.main_page.search_product(current_user.eBook)

        with allure.step("Add selected product to wishlist"):
            app.main_page.add_to_wishlist()
        # THEN
        with allure.step("Delete selected product from wishlist"):
            app.main_page.delete_from_wishlist()

    @pytest.mark.product
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('ADD TO CART')
    @allure.severity(Severity.CRITICAL)
    def test_select_product_with_params(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Search product"):
            app.main_page.search_product(current_user.search_product)

        with allure.step("Select product model"):
            app.select_product.select_model(current_user.phone_model)

        with allure.step("Confirm selected choice"):
            app.select_product.confirm_selection()
        # THEN
        with allure.step("Check correct product on the page"):
            app.select_product.check_selection(current_user.phone_model)

    @pytest.mark.city
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('GEO')
    @allure.severity(Severity.CRITICAL)
    def test_geo_change(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Select user city"):
            app.main_page.select_city(current_user.city)
        # THEN
        with allure.step("Check selected city"):
            app.main_page.check_selected(current_user.city)

    @pytest.mark.feedback
    @allure.tag('UI', 'WEB')
    @allure.description('DNS UI test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('UI')
    @allure.story('GEO')
    @allure.severity(Severity.NORMAL)
    def test_feedback(self,selenoid_config):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()
        # WHEN
        with allure.step("Open authorization window"):
            app.auth.open_login_window()

        with allure.step("Select feedback option"):
            app.main_page.select_feedback()

        with allure.step("Select question to ask"):
            app.feedback.select_question(current_user.question)

        with allure.step("Select item to ask"):
            app.feedback.select_item(current_user.item)

        with allure.step("Fill message to ask"):
            app.feedback.fill_message(current_user.random_text)

        with allure.step("Fill user name"):
            app.feedback.fill_name(current_user.first_name)

        with allure.step("Fill user email"):
            app.feedback.fill_email(current_user.random_email)
        # THEN
        with allure.step("Check submite button activate"):
            app.feedback.check_button_activate()

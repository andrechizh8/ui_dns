from selene.support.shared import browser
from selene import have,be
import time
from model.utils.helpers import path_to
from model.controls.base_controls import DatePicker


class ProfilePage:

    def open_profile_settings(self):
        browser.all(".user-menu__common-link.user-menu__common-link_child").element_by(
            have.text("Настройки профиля")).click()
        return self

    def set_avatar(self, path):
        browser.element("[class$='wrapper_editable']").click()
        path_to("[type='file']", path)
        time.sleep(2)
        browser.element("//*[@class='submit-btns']/button[2]").click().press_enter()
        return self

    def fill_first_name(self, first_name):
        browser.driver.refresh()
        time.sleep(2)
        browser.element('[name="ProfileSettingsForm[firstname]"]').clear().type(first_name)
        return self

    def fill_last_name(self, last_name):
        browser.element('[name="ProfileSettingsForm[lastname]"]').clear().type(last_name)
        return self

    def fill_nickname(self, nickname):
        browser.element('[name="ProfileSettingsForm[nickname]"]').clear().type(nickname)
        return self

    def fill_birthday(self, date):
        DatePicker(browser.element('[name="ProfileSettingsForm[birthdate]"]')).set_date(date)
        time.sleep(3)
        browser.element(".logo-container__logo").click()
        return self

    def check_nickname_change(self):
        nickname = browser.element('[name="ProfileSettingsForm[nickname]"]')().get_attribute('value')
        browser.element('.user-settings-info__nickname').should(have.text(nickname))
        time.sleep(3)
        browser.element(".logo-container__logout").click()
        return self

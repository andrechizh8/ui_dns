import time
from selene import have, be
from selene.support.shared import browser



class Authorization:
    def open_login_window(self):
        browser.element("//div[text()[contains(.,'Войти')]]").click()
        return self

    def select_enter_button(self):
        browser.element("//*[@class='user-profile__guest']/button").click()
        browser.element(".block-other-login-methods__password-caption").click()
        return self

    def fill_email_input(self, value):
        browser.element(".base-ui-input-row__input.base-ui-input-row__input_with-icon").type(value)
        time.sleep(2)
        return self

    def fill_password_input(self, value):
        browser.element("//*[contains(@type,'password')]").type(value)
        browser.element("[class$='ui-button-v2']").with_(timeout=3).should(be.clickable).click()
        time.sleep(2)
        return self

    def open_user_cabinet(self):
        browser.element(".user-profile__avatar").click()
        return self

    def check_log_in(self):
        browser.all("[class$='link_child']").element_by(have.text("Настройки профиля")).should(be.visible)
        return self

    def open_logout_window(self):
        browser.element(".user-profile__avatar").click()
        return self

    def click_logout(self):
        browser.all("[class$='link_child']").element_by(have.text("Выйти")).click()
        time.sleep(2)
        return self

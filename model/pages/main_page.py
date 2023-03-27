import time
from selene.support.shared import browser
from selene import be, have


class MainPage:

    def search_product(self, value):
        browser.element(".presearch__input").send_keys(value).press_enter()
        return self

    def add_to_wishlist(self):
        browser.element("button.button-ui.button-ui_white.button-ui_icon.wishlist-btn").with_(timeout=10).should(
            be.clickable).click()
        browser.element(".ui-link.ui-link_gray_dark").click()
        browser.element(".wishlist-link-counter").with_(timeout=3).should(be.clickable).click()
        browser.element("[class^='catalog-products']").should(
            have.text('6" Электронная книга Digma K2 серый [758x1024, E-Ink Pearl, подсветка, 1500 мА*ч]'))
        return self

    def delete_from_wishlist(self):
        browser.element("[class$='select-all']").click()
        browser.element("[class$='controls_delete']").click()
        browser.element(".profile-wishlist__sum").should(have.text("0 товаров на сумму: 0 ₽"))
        return self

    def select_city(self, value):
        browser.element(".city-select__text_BTU").click()
        browser.all(".city-bubble_IBz").element_by(have.text(value)).click()
        return self

    def check_selected(self, value):
        browser.element(".city-select__text_BTU").should(have.text(value))
        return self

    def select_feedback(self):
        time.sleep(2)
        browser.all(".user-menu__common-link.user-menu__common-link_child").element_by(
            have.text("Обратная связь")).click()
        return self

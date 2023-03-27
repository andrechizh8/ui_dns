from selene.support.shared import browser
from selene import have
from model.controls.base_controls import CheckBox
from model.utils.helpers import scroll_to_element


class ProductSelectPage:

    def select_model(self, value):
        browser.execute_script("window.scrollTo(0,1500)")
        CheckBox(browser.all("//label[@class='ui-checkbox ui-checkbox_list']")).set_checkbox(value)
        return self

    def confirm_selection(self):
        scroll_to_element("[class$='brand left-filters__button']")
        browser.element("[class$='brand left-filters__button']").click()
        return self

    def check_selection(self, model):
        browser.element("[class^='catalog-product__name']").should(have.text(model))
        return self

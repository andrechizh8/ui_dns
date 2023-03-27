from selene.support.shared import browser
from selene import be
from model.controls.base_controls import DropDown, RadioButton
from model.utils.helpers import scroll_to_element


class FeedbackPage:

    def select_question(self, value):
        DropDown(browser.element(".select2-selection__arrow")).set_dropdown(".select2-search__field", value)
        return self

    def select_item(self, value):
        browser.execute_script("window.scrollTo(0,1500)")
        RadioButton(browser.all(".ui-radio__item")).set_radio(value)
        return self

    def fill_message(self, value):
        browser.execute_script("window.scrollTo(0,2000)")
        browser.element("[name='TicketCreateForm[text]']").type(value)
        return self

    def fill_name(self, value):
        browser.element("[name='TicketCreateForm[userName]'").type(value)
        return self

    def fill_email(self, value):
        browser.element("[name='TicketCreateForm[userEmail]'").type(value)
        return self

    def check_button_activate(self):
        scroll_to_element(".form__agree-text")
        browser.element("[class$='form__submit-button']").should(be.clickable)
        return self

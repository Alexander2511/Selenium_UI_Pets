from .base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from data.data import RegisterPageData
from generator.generator import Generator


class RegisterPage(BasePage):
    def input_mail(self):
        input_email = self.browser.find_element(*RegisterPageLocators.LOGIN_INPUT)
        input_email.send_keys(RegisterPageData.LOGIN)

    def input_pass(self):
        input_pass = self.browser.find_element(*RegisterPageLocators.INPUT_PASS)
        input_pass.send_keys(RegisterPageData.PASS)

    def confirm_pass(self):
        confirm_pass = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASS)
        confirm_pass.send_keys(RegisterPageData.PASS)

    def submit_btn(self):
        sbt_btn = self.browser.find_element(*RegisterPageLocators.SUBMIT_BTN)
        sbt_btn.submit()

    def show_pass(self):
        pass_visibility = self.browser.find_element(*RegisterPageLocators.TOGGLE_PASS_VISIBILITY)
        pass_visibility.click()

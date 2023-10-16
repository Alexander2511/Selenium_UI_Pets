from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data.data import LoginPageData


class LoginPage(BasePage):
    def enter_login(self, email):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(email)

    def enter_valid_login(self):
        valid_login = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        valid_login.send_keys(LoginPageData.VALID_EMAIL)

    def enter_pass(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys(LoginPageData.VALID_PASS)

    def submit_btn(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()

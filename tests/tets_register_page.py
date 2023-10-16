from data.data import RegisterPageData, LoginPageData
from pages.register_page import RegisterPage
from locators.profile_page_locators import ProfilePageLocators
from locators.register_page_locators import RegisterPageLocators
import pytest


@pytest.mark.smoke
def test_register(browser):
    page = RegisterPage(browser, RegisterPageData.REGISTER_PAGE_URL)
    page.open()
    page.input_email()
    page.input_pass()
    page.show_pass()
    page.confirm_pass()
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/new_user.png")
    page.submit_btn()
    page.element_is_visible(ProfilePageLocators.ADD_PET_BTN)


@pytest.mark.parametrize("email", LoginPageData.INCORRECT_EMAILS)
@pytest.mark.regression
def test_register_with_incorrect_email(browser, email):
    page = RegisterPage(browser, RegisterPageData.REGISTER_PAGE_URL)
    page.open()
    page.input_emails(email)
    page.input_pass()
    page.show_pass()
    page.confirm_pass()
    page.submit_btn()
    page.element_is_visible(RegisterPageLocators.FIELD_IS_EMAIL, 5)
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/register_bad_email.png")

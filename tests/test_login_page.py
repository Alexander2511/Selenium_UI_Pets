from data.data import LoginPageData
from pages.login_page import LoginPage
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
import pytest


@pytest.mark.parametrize("email", LoginPageData.VALID_EMAILS)
@pytest.mark.smoke
def test_login(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    page.element_is_visible(ProfilePageLocators.ADD_PET_BTN, 5)
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/login.png")


@pytest.mark.parametrize("email", LoginPageData.INVALID_EMAILS)
@pytest.mark.smoke
def test_login_with_unregistered_email(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    page.element_is_visible(LoginPageLocators.WRONG, 5)
    browser.save_screenshot("C:/Users/freed/PycharmProjects//Selenium_UI_Pets/screenshots/login_1.png")


@pytest.mark.parametrize("email", LoginPageData.INCORRECT_EMAILS)
@pytest.mark.regression
def test_login_with_incorrect_email(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    page.submit_btn()
    page.element_is_visible(LoginPageLocators.FIELD_IS_EMAIL, 5)
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/login_2.png")

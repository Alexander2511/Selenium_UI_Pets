from data.data import RegisterPageData, ProfilePageData
from pages.register_page import RegisterPage
from locators.profile_page_locators import ProfilePageLocators
import pytest
import requests


@pytest.mark.smoke
def test_register(browser):
    page = RegisterPage(browser, RegisterPageData.REGISTER_PAGE_URL)
    page.open()
    page.input_mail()
    page.input_pass()
    page.show_pass()
    page.confirm_pass()
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/new_user.png")
    page.submit_btn()
    page.element_is_visible(ProfilePageLocators.ADD_PET_BTN)
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200

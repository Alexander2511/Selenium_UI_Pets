from data.data import LoginPageData, ProfilePageData
from pages.login_page import LoginPage
import requests
import pytest
import time


@pytest.mark.parametrize("email", [LoginPageData.VALID_EMAIL, LoginPageData.INVALID_EMAIL])
@pytest.mark.smoke
def test_login(browser, email):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login(email)
    page.enter_pass()
    time.sleep(3)
    page.submit_btn()
    time.sleep(4)
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/login_result.png")

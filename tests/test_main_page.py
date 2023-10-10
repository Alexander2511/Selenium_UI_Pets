from pages.main_page import MainPage
from data.data import MainPageData, ProfilePageData, LoginPageData
import requests
import pytest
import time


@pytest.mark.smoke
def test_go_to_profile_page(browser, login):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.click_logo_btn()
    time.sleep(4)
    page.go_to_profile()
    response = requests.get(ProfilePageData.PROFILE_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.xfail
def test_logout(browser, login):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.click_logo_btn()
    page.logout()
    response = requests.get(LoginPageData.LOGIN_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.smoke
def test_filter_pet_by_type(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_type()
    page.go_to_cat_list()
    time.sleep(3)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/filter_cat.png')


@pytest.mark.smoke
def test_filter_by_pet_name(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.filter_by_name()
    page.enter_pet_name()
    time.sleep(3)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/filter_by_name.png')


@pytest.mark.smoke
def test_pet_detail(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.go_to_details()
    time.sleep(2)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/pet_detail.png')


@pytest.mark.skip('Нужно добавить создание питомца')
def test_like(browser, login, new_pet):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.click_logo_btn()
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/like_pet_before.png')
    page.like_pet()
    time.sleep(2)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/like_pet_after.png')


@pytest.mark.regression
def test_go_to_last_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.go_to_last_page()
    time.sleep(2)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/last_page.png')


@pytest.mark.regression
def test_go_to_next_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    time.sleep(1)
    page.go_to_next_page()
    time.sleep(2)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/next_page.png')


@pytest.mark.regression
def test_go_to_first_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.go_to_last_page()
    time.sleep(2)
    page.go_to_first_page()
    time.sleep(1)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/first_page.png')


@pytest.mark.regression
def test_go_to_previous_page(browser):
    page = MainPage(browser, MainPageData.MAIN_PAGE_URL)
    page.open()
    page.open()
    page.go_to_last_page()
    time.sleep(2)
    page.go_to_previous_page()
    time.sleep(2)
    browser.save_screenshot('C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/previous_page.png')

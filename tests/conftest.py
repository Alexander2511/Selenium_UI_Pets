from selenium import webdriver
from pages.login_page import LoginPage
from pages.new_pet_page import NewPetPage
from data.data import LoginPageData, NewPetData
import time
import pytest


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    page = LoginPage(browser, LoginPageData.LOGIN_PAGE_URL)
    page.open()
    page.enter_login()
    page.enter_pass()
    time.sleep(3)
    page.submit_btn()
    time.sleep(3)


@pytest.fixture()
def new_pet(browser, login):
    page = NewPetPage(browser, NewPetData.NEW_PET_PAGE_URL)
    page.open()
    page.input_name()
    page.click_type_dropdown()
    page.choose_type()
    page.input_age()
    page.click_gender()
    page.choose_male_gender()
    page.submit_btn()
    page.input_img()
    page.send_img()


from pages.profile_page import ProfilePage
from data.data import LoginPageData, ProfilePageData, NewPetData, MainPageData, PetEditPage
import requests
import pytest
import time


@pytest.mark.smoke
def test_quit_profile(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_quit_btn()
    time.sleep(3)
    response = requests.get(LoginPageData.LOGIN_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.smoke
def test_go_to_add_pet_page(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_add_pet()
    time.sleep(3)
    response = requests.get(NewPetData.NEW_PET_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.skip
def test_delete_profile(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.delete_profile()
    time.sleep(3)
    response = requests.get(LoginPageData.LOGIN_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_go_to_main_page(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.click_logo_btn()
    response = requests.get(MainPageData.MAIN_PAGE_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_go_to_pet_edit(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.edit_pet()
    time.sleep(2)
    response = requests.get(PetEditPage.PET_EDIT_URL)
    assert response.status_code == 200


@pytest.mark.regression
def test_delete_pet(browser, login):
    page = ProfilePage(browser, ProfilePageData.PROFILE_PAGE_URL)
    page.open()
    page.delete_pet()
    time.sleep(2)
    response = requests.get(PetEditPage.PET_EDIT_URL)
    assert response.status_code == 200



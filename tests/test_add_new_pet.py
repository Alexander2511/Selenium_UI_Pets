from pages.new_pet_page import NewPetPage
from locators.new_pet_page_locators import NewPetLocators
from locators.profile_page_locators import ProfilePageLocators
from data.data import NewPetData
import time
import pytest


@pytest.mark.smoke
def test_add_new_pet(browser, login):
    page = NewPetPage(browser, NewPetData.NEW_PET_PAGE_URL)
    page.open()
    page.input_name()
    page.click_type_dropdown()
    page.choose_type()
    page.input_age()
    page.click_gender()
    page.choose_male_gender()
    page.submit_btn()
    page.element_is_visible(NewPetLocators.SEND_IMG, 5)
    page.input_img()
    page.send_img()
    page.element_is_visible(ProfilePageLocators.POP_UP)
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/new_pet.png")


@pytest.mark.smoke
def test_cancel_adding_pet(browser, login):
    page = NewPetPage(browser, NewPetData.NEW_PET_PAGE_URL)
    page.open()
    page.input_name()
    time.sleep(2)
    page.click_type_dropdown()
    page.choose_type()
    time.sleep(2)
    page.input_age()
    page.click_gender()
    page.choose_male_gender()
    page.cancel_btn()
    time.sleep(2)
    browser.save_screenshot("C:/Users/freed/PycharmProjects/Selenium_UI_Pets/screenshots/cancel.png")

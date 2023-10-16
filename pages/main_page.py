from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from data.data import MainPageData


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(*MainPageLocators.REGISTER_LINK)
        register_link.click()

    def filter_by_type(self):
        pet_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        pet_type.click()

    def filter_by_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        pet_name.click()

    def go_to_next_page(self):
        next_page = self.browser.find_element(*MainPageLocators.NEXT_PAGE)
        next_page.click()

    def go_to_last_page(self):
        last_page = self.browser.find_element(*MainPageLocators.LAST_PAGE)
        last_page.click()

    def go_to_previous_page(self):
        previous_page_btn = self.browser.find_element(*MainPageLocators.PREVIOUS_PAGE_BTN)
        previous_page_btn.click()

    def go_to_first_page(self):
        first_page = self.browser.find_element(*MainPageLocators.FIRS_PAGE_BTN)
        first_page.click()

    def go_to_third_page(self):
        third_page = self.browser.find_element(*MainPageLocators.THIRD_BTN)
        third_page.click()

    def go_to_details(self):
        details = self.browser.find_element(*MainPageLocators.DETAILS_BTN)
        details.click()

    def like_pet(self):
        like = self.browser.find_element(*MainPageLocators.LIKE_BTN)
        like.click()

    def go_to_dog_list(self):
        dog_list = self.browser.find_element(*MainPageLocators.DOG_CATEGORY)
        dog_list.click()

    def go_to_cat_list(self):
        cat_list = self.browser.find_element(*MainPageLocators.CAT_CATEGORY)
        cat_list.click()

    def go_to_reptile_list(self):
        reptile_list = self.browser.find_element(*MainPageLocators.REPTILE_CATEGORY)
        reptile_list.click()

    def go_to_hamster_list(self):
        hamster_list = self.browser.find_element(*MainPageLocators.HAMSTER_CATEGORY)
        hamster_list.click()

    def go_to_parrot_list(self):
        parrot_list = self.browser.find_element(*MainPageLocators.PARROT_CATEGORY)
        parrot_list.click()

    def go_to_profile(self):
        profile_button = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        profile_button.click()

    def click_logo_btn(self):
        logo_btn = self.browser.find_element(*MainPageLocators.LOGO)
        logo_btn.click()

    def logout(self):
        logout = self.browser.find_element(*MainPageLocators.QUIT_BTN)
        logout.click()

    def enter_pet_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        pet_name.send_keys(MainPageData.PET_NAME)
        pet_name.send_keys(Keys.ENTER)

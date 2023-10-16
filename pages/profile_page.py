from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def click_logo_btn(self):
        logo_btn = self.browser.find_element(*ProfilePageLocators.LOGO)
        logo_btn.click()

    def click_quit_btn(self):
        quit_btn = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_btn.click()

    def click_add_pet(self):
        add_btn = self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN)
        add_btn.click()

    def delete_profile(self):
        del_btn = self.browser.find_element(*ProfilePageLocators.DEL_PROFILE_BTN)
        del_btn.click()

    def edit_pet(self):
        edit_btn = self.browser.find_element(*ProfilePageLocators.EDIT_PET_BTN)
        edit_btn.click()

    def delete_pet(self):
        delete_pet_btn = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BTN)
        delete_pet_btn.click()

    def confirm_deleting(self):
        confirm_btn = self.browser.find_element(*ProfilePageLocators.CONFIRM_BTN)
        confirm_btn.click()

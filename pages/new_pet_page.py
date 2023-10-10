from .base_page import BasePage
from locators.new_pet_page_locators import NewPetLocators
from data.data import NewPetData
from selenium.webdriver.common.by import By


class NewPetPage(BasePage):
    def input_name(self):
        pet_name = self.browser.find_element(*NewPetLocators.PET_NAME)
        pet_name.send_keys(*NewPetData.PET_NAME)

    def click_type_dropdown(self):
        dropdown = self.browser.find_element(*NewPetLocators.TYPE_DROPDOWN)
        dropdown.click()

    def choose_type(self):
        pet_type = self.browser.find_element(*NewPetLocators.TYPE_PET)
        pet_type.click()

    def input_age(self):
        pet_age = self.browser.find_element(*NewPetLocators.INPUT_AGE)
        pet_age.send_keys(*NewPetData.PET_AGE)

    def click_gender(self):
        pet_gender = self.browser.find_element(*NewPetLocators.PETS_GENDER)
        pet_gender.click()

    def choose_male_gender(self):
        male_gender = self.browser.find_element(By.XPATH, '//div[3]/div/ul/li[1]')
        male_gender.click()

    def submit_btn(self):
        submit_btn = self.browser.find_element(*NewPetLocators.SUBMIT_BTN)
        submit_btn.submit()

    def cancel_btn(self):
        cancel_btn = self.browser.find_element(*NewPetLocators.CANCEL_BTN)
        cancel_btn.click()

    def input_img(self):
        choose_img = self.browser.find_element(*NewPetLocators.INPUT_IMG)
        choose_img.send_keys(*NewPetData.IMG_LINK)

    def send_img(self):
        send_img = self.browser.find_element(*NewPetLocators.SEND_IMG)
        send_img.click()




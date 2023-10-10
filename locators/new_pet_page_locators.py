from selenium.webdriver.common.by import By


class NewPetLocators:
    PET_NAME = (By.ID, 'name')
    TYPE_DROPDOWN = (By.ID, 'typeSelector')
    INPUT_AGE = (By.XPATH, '//*[@id="age"]/input[1]')
    PETS_GENDER = (By.ID, 'genderSelector')
    GENDER_MALE = (By.XPATH, '//div[3]/div[1]/ul[1]/li[1]')
    GENDER_FEMALE = (By.XPATH, '//div[3]/div/ul/li[1]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[1]')
    CANCEL_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[2]')
    TYPE_PET = (By.XPATH, '//div[3]/div/ul/li[3]')
    INPUT_IMG = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    SEND_IMG = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div')

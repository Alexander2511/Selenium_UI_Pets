from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div')
    QUIT_BTN = (By.CSS_SELECTOR, 'li:nth-child(2) a:nth-child(1)')
    ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
    DEL_PROFILE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
    EDIT_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]')
    DELETE_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]')
    CONFIRM_BTN = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(3) > div:nth-of-type(2) > button:nth-of-type(2)')
    POP_UP = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(2) > div > div > div')

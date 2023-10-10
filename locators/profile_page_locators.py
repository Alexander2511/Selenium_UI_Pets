from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LOGO = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/div[1]/images[1]')
    QUIT_BTN = (By.CSS_SELECTOR, 'li:nth-child(2) a:nth-child(1)')
    ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
    DEL_PROFILE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
    EDIT_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]')
    DELETE_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]')
    CONFIRM_BTN = (By.XPATH, 'body/div[3]/div[2]/button[2]')

from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, 'div#pv_id_11_content > div > form > div:nth-of-type(3) > button')
    TOGGLE_PASS_VISIBILITY = (By.XPATH, '//*[@id="password"]/i[1]')
    LOGO = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/div[1]/images[1]')
    DETAILS_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]')

from selenium.webdriver.common.by import By


class RegisterPageLocators:

    LOGIN_INPUT = (By.ID, "login")
    INPUT_PASS = (By.CSS_SELECTOR, "#password > input")
    CONFIRM_PASS = (By.CSS_SELECTOR, "#confirm_password > input")
    SUBMIT_BTN = (By.CLASS_NAME, "p-button-label")
    TOGGLE_PASS_VISIBILITY = (By.XPATH, '//*[@id="password"]/i[1]')

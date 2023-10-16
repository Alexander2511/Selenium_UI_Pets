from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    REGISTER_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(2) > a > span")
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    FILTER_BY_NAME = (By.ID, 'petName')
    DOG_CATEGORY = (By.ID, 'pv_id_2_0')
    CAT_CATEGORY = (By.ID, 'pv_id_2_1')
    REPTILE_CATEGORY = (By.ID, 'pv_id_2_2')
    HAMSTER_CATEGORY = (By.ID, 'pv_id_2_3')
    PARROT_CATEGORY = (By.ID, 'pv_id_2_4')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div')
    NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/button[3]')
    LAST_PAGE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/button[4]/span[1]')
    PREVIOUS_PAGE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/button[2]')
    FIRS_PAGE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/button[1]')
    THIRD_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/span[1]/button[3]')
    DETAILS_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]')
    LIKE_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/span[1]/i[1]')
    PROFILE_BTN = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]')
    QUIT_BTN = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[2]/a[1]')

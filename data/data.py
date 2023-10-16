from  datetime import datetime
current_datetime = datetime.now()


class MainPageData:
    MAIN_PAGE_URL = 'http://34.141.58.52:8080/#/'
    PET_NAME = "Cooper"


class LoginPageData:
    LOGIN_PAGE_URL = 'http://34.141.58.52:8080/#/login'
    VALID_EMAIL = 'test@dog.com'
    VALID_EMAILS = ['test@dog.com', 'test1@dog.com']
    VALID_PASS = 'Xx@12345'
    INVALID_PASS = '12345'
    INVALID_EMAILS = ['ups@net.com', 'issue@net.py']
    INCORRECT_EMAILS = ['test.test.net', 'tut@domcom']


class ProfilePageData:
    PROFILE_PAGE_URL = 'http://34.141.58.52:8080/#/profile'


class NewPetData:
    NEW_PET_PAGE_URL = 'http://34.141.58.52:8080/#/pet-new/pet'
    NEW_PET_AVA_URL = 'http://34.141.58.52:8080/#/pet-new/%/ava'
    PET_NAME = "Sugar"
    PET_AGE = "3"
    IMG_LINK = r"C:\Users\freed\PycharmProjects\Selenium_UI_Pets\images\Dino1.jpg"


class PetEditPage:
    PET_EDIT_URL = 'http://34.141.58.52:8080/#/pet-edit/%'


class RegisterPageData:
    REGISTER_PAGE_URL = 'http://34.141.58.52:8080/#/register'
    LOGIN = f'{current_datetime.microsecond}@dog.com'
    PASS = 'Xx@12345'

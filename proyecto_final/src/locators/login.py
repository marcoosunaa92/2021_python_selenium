from selenium.webdriver.common.by import By


class LoginPageLoc:
    USER = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN = (By.ID, 'login-button')
    ERROR_MSG = (By.XPATH, "//*[@data-test='error']")
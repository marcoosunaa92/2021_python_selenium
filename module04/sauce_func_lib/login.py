import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from module04.sauce_func_lib.common import write_to_input, click


def login(wait: WebDriverWait, user: str, password: str):
    write_to_input(wait, (By.ID, 'user-name'), user)
    write_to_input(wait, (By.ID, 'password'), password)
    click(wait, (By.ID, 'login-button'))


def get_login_error(wait: WebDriverWait):
    pass

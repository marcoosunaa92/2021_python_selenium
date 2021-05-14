import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common import get_driver
from module04.sauce_func_lib.inventory import get_inventory
from module04.sauce_func_lib.login import login

DATA = [
    ('standard_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
]


@pytest.mark.sanity
@pytest.mark.parametrize('user, password', DATA)
def test_login_valid_user(user, password):
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, user, password)
    get_inventory(wait)
    items = get_inventory(wait)
    assert len(items) > 0
    driver.quit()


@pytest.mark.skip(reason='test')
def test_login_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid_password')
    with pytest.raises(TimeoutException):
        get_inventory(wait)
    driver.quit()

import pytest
from proyecto_final.src.pages.login import LoginPage
from proyecto_final.tests.common.test_base import TestBase

LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce')
]

ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'


LOGIN_DATA = [
    ('standard_user', 'secret_sauce'),
    ('performance_glitch_user', 'secret_sauce'),
    ('problem_user', 'secret_sauce'),
]


ERROR_MSG = 'Epic sadface: Username and password do not match any user in this service'


class TestLogin(TestBase):

    @pytest.mark.skip
    @pytest.mark.parametrize('user, password', LOGIN_DATA)
    def test_valid_user(self, user: str, password: str):
        page = LoginPage(self.driver)
        page.open()
        page.login(user, password)

    @pytest.mark.skip
    @pytest.mark.login
    def test_invalid_user(self):
        page = LoginPage(self.driver)
        page.open()
        page.login('standard_user', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == ERROR_MSG, f'Error message should be {ERROR_MSG}'

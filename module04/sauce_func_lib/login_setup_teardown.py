from selenium.webdriver.support.wait import WebDriverWait

from common import get_driver


class login_setup_teardown:
    def setup_method(self):
        self.driver = get_driver('chrome')
        self.wait = WebDriverWait(self, self.driver, 5)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

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

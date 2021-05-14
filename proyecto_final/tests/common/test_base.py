from common.webdriver_factory import get_driver


class TestBase:
    def setup_method(self):
        self.driver = get_driver('chrome')

    def teardown_method(self):
        if self.driver:
            self.driver.close()

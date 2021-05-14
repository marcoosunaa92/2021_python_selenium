from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement:

    def __init__(self, loc: tuple, wait: WebDriverWait = None, root: WebElement = None):
        self._wait = wait
        self._loc = loc
        self._root = root

    def wait_until_loaded(self) -> WebElement:
        if self._root and isinstance(self._root, WebElement):
            return self._root.find_element(*self._loc)
        elif self._wait and isinstance(self._wait, WebDriverWait):
            return self._wait.until(EC.element_to_be_clickable(self._loc))
        else:
            raise ValueError('Page element must have either an instance or wait or a root WebElement')

    def click(self):
        element = self.wait_until_loaded()
        element.click()

    def write(self, value):
        element = self.wait_until_loaded()
        element.clear
        element.send_keys(value)

    def get_value(self) -> str:
        element = self.wait_until_loaded()
        return element.get_attribute('Value')

    def get_text(self) -> str:
        """Get value attribute."""
        element = self.wait_until_loaded()
        return element.text

from selenium.webdriver.remote.webdriver import WebDriver

from proyecto_final.src.elements.base_page_element import BasePageElement
from proyecto_final.src.elements.header import Header
from proyecto_final.src.elements.inventory_items import InventoryItems
from proyecto_final.src.locators.check_out import CheckOutLoc
from proyecto_final.src.pages.base_page import BasePage
from proyecto_final.src.pages.inventory import InventoryPage

_URL = 'https://www.saucedemo.com/cart.html'


class CheckOutPage(BasePage):
    """Implements inventory item details"""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.products = InventoryItems(CheckOutLoc.ITEMS, self._wait)
        self.__label = BasePageElement(CheckOutLoc.LABEL, self._wait)
        self._continue_shopping_btn = BasePageElement(CheckOutLoc.CONTINUE_SHOPPING_BTN, self._wait)
        self.check_out_btn = BasePageElement(CheckOutLoc.CHECK_OUT_BTN, self._wait)
        self.header = Header(self._wait)

    def continue_shopping(self):
        """Go back to details page."""
        self._continue_shopping_btn.click()
        return InventoryPage(self._driver, self._timeout)

    def check_out(self):
        self.check_out_btn.click()
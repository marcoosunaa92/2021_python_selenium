from selenium.webdriver.remote.webdriver import WebDriver

from proyecto_final.src.elements.base_page_element import BasePageElement
from proyecto_final.src.elements.header import Header
from proyecto_final.src.locators.inventory_details import InventoryDetailsLoc
from proyecto_final.src.mixin.inventoryItemMixin import InventoryItemMixin
from proyecto_final.src.pages.base_page import BasePage

_URL = 'https://www.saucedemo.com/inventory-item.html?id={0}'


class InventoryDetailsPage(InventoryItemMixin, BasePage):
    """Implements inventory item details"""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._title = BasePageElement(InventoryDetailsLoc.TITLE, wait=self._wait)
        self._description = BasePageElement(InventoryDetailsLoc.DESCRIPTION, wait=self._wait)
        self._price = BasePageElement(InventoryDetailsLoc.PRICE, wait=self._wait)
        self._inv_btn = BasePageElement(InventoryDetailsLoc.BTN, wait=self._wait)
        self._back_btn = BasePageElement(InventoryDetailsLoc.BACK_BTN, wait=self._wait)
        self.header = Header(self._wait)

    def back(self):
        """Go back to details page."""
        self._back_btn.click()
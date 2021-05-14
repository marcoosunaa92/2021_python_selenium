from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from proyecto_final.src.elements.base_page_element import BasePageElement
from proyecto_final.src.locators.inventory_Item import InventoryItemLoc
from proyecto_final.src.mixin.inventoryItemMixin import InventoryItemMixin
from proyecto_final.src.pages.inventoryItemDetails import InventoryDetailsPage


class InventoryItem(InventoryItemMixin):
    """Represents inventory item."""

    def __init__(self, wait: WebDriverWait, root: WebElement):
        self._wait = wait
        self._title = BasePageElement(InventoryItemLoc.TITLE, wait=wait, root=root)
        self._image = BasePageElement(InventoryItemLoc.IMG, wait=wait, root=root)
        self._description = BasePageElement(InventoryItemLoc.DESCRIPTION, wait=wait, root=root)
        self._price = BasePageElement(InventoryItemLoc.PRICE, wait=wait, root=root)
        self._inv_btn = BasePageElement(InventoryItemLoc.BTN, wait=wait, root=root)

    def click_on_image(self) -> str:
        self._image.click()
        return InventoryDetailsPage(self._wait._driver, self._wait._timeout)

    def click_on_title(self):
        """Open product details"""
        self._title.click()
        return InventoryDetailsPage(self._wait._driver, self._wait._timeout)

    def add_to_cart(self):
        self._inv_btn.click()
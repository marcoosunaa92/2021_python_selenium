from enum import Enum
from proyecto_final.src.elements.base_page_element import BasePageElement
from proyecto_final.src.elements.header import Header
from proyecto_final.src.elements.inventory_items import InventoryItems
from proyecto_final.src.locators.inventory import InventoryPageLoc
from proyecto_final.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from proyecto_final.src.elements.select_element import SelectElement

_URL = 'https://www.saucedemo.com/inventory.html'


class InventorySortOptions(Enum):
    A_TO_Z = 'az'
    Z_TO_A = 'za'
    PRICE_LOW_TO_HIGH = 'lohi'
    PRICE_HIGH_TO_LOW = 'hilo'


class InventoryPage(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)

        self.products = InventoryItems(InventoryPageLoc.ITEMS, self._wait)
        self.__label = BasePageElement(InventoryPageLoc.LABEL, self._wait)
        self.__sort_dropdown = SelectElement(InventoryPageLoc.SORT_DROPDOWN, self._wait)
        self.header = Header(self._wait)

    def get_label(self) -> str:
        """Get page label."""
        return self.__label.get_text()

    def sort_by(self, option: InventorySortOptions):
        """Sort by specified value"""
        self.__sort_dropdown.get_select_instance().select_by_value(option)

    def get_sort_value(self) -> str:
        """Get select sort value."""
        return self.__sort_dropdown.get_select_instance().first_selected_option.get_attribute('value')
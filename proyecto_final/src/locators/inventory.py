from selenium.webdriver.common.by import By


class InventoryPageLoc:
    """Inventory page locators."""
    CART = (By.CLASS_NAME, 'cart_item')
    ITEMS = (By.CLASS_NAME, 'inventory_item')
    LABEL = (By.CLASS_NAME, 'title')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
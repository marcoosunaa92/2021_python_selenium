from selenium.webdriver.common.by import By


class CheckOutLoc:
    """Inventory item locators.
    Locators are relative to parent container div.
    """
    ITEMS = (By.CLASS_NAME, 'cart_item')
    LABEL = (By.CLASS_NAME, 'title')
    CONTINUE_SHOPPING_BTN = (By.ID, 'continue-shopping')
    CHECK_OUT_BTN = (By.ID, 'checkout')

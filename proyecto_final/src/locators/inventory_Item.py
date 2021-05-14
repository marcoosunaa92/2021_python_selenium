from selenium.webdriver.common.by import By


class InventoryItemLoc:
    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    IMG = (By.CLASS_NAME, 'inventory_item_img')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    BTN = (By.XPATH, ".//button[contains(@class,'btn_inventory')]")
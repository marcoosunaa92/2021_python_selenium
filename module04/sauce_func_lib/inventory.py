from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


def get_inventory(wait: WebDriverWait) -> list:
    locator = (By.XPATH, '//div[@class= "inventory_item"]')
    elements = wait.until(EC.visibility_of_all_elements_located(locator))
    items_list = []
    for element in elements:
        title = element.find_element_by_xpath('.//div[@class= "inventory_item_name"]')
        items_list.append(title.text)
    return items_list

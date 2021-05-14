from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def write_to_input(wait: WebDriverWait, locator: By, value: str):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.clear()
    element.send_keys(value)


def click(wait: WebDriverWait, locator: By):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

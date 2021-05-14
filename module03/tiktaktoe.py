import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from common import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def winner():
    try:
        locator = (By.XPATH, "//*[contains(@class, 'restart')]")
        my_wait.until(EC.visibility_of_element_located(locator))
        return True
    except:
        return False


def print_stats():
    pass


def select_tile():
    try:
        locator = (By.XPATH, "//*[contains(@class, 'square')]")
        tiles = my_wait.until(EC.visibility_of_all_elements_located(locator))
        tiles: WebElement
        empty = []
        for tile in tiles:
            tile: WebElement
            cell = tile.find_element_by_tag_name('div')
            if not cell.get_attribute('class'):
                empty.append(tile)
        target = random.choice(empty)
        target: WebElement
        target.click()
    except TimeoutException as exception:
        raise RuntimeError(f'No empty tiles.{exception}')


driver = get_driver('chrome')
my_wait = WebDriverWait(driver, 1)
driver.get('https://playtictactoe.org/')
while not winner():
    select_tile()
print_stats()
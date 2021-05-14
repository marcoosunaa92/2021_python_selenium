from selenium.webdriver.remote.webelement import WebElement
from common import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def search(my_wait: WebDriverWait, value: str):
    locator = (By.NAME, 'q')
    textbox_locator = my_wait.until(EC.element_to_be_clickable(locator))
    textbox_locator.clear()
    textbox_locator.send_keys(value)

    locator = (By.XPATH, "//button[@type='submit']")
    button_locator = my_wait.until(EC.element_to_be_clickable(locator))
    button_locator.click()


def print_results(my_wait: WebDriverWait):
    locator = (By.XPATH, "//a[contains(@class, 'result-item')]")
    profile_locator = my_wait.until(EC.visibility_of_all_elements_located(locator))
    profile: WebElement
    for profile in profile_locator:
        title = profile.find_element_by_xpath(".//p[contains(@class, ' title' )]")
        description = profile.find_element_by_xpath()
        print(f'{title.text} | {description.text}')


driver = get_driver('chrome')
my_wait = WebDriverWait(driver, 5)
driver.get('https://www.tiktok.com')

search(my_wait, 'Python')
print_results(my_wait)


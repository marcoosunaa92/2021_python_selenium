from proyecto_final.src.pages.base_page import BasePage
from common.webdriver_factory import get_driver

def test_page_base():
    driver = get_driver('chrome')
    page = BasePage(driver, 'https://google.com')
    page.open()
    page.wait_until_loaded()
    page.timeout = 5
    assert page.timeout == 5, 'Page timeout should be 10'
    page.close()


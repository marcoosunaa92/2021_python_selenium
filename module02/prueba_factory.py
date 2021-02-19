from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://google.com')
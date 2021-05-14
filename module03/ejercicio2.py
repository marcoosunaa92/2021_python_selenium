from common import get_driver
from selenium.webdriver.support.wait import WebDriverWait

driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.google.com/')
driver.implicitly_wait(10)


driver.find_element_by_xpath('//body/div[1]')
driver.find_element_by_xpath('//body/div[last()]')


from common import get_driver
from selenium.webdriver.support.wait import WebDriverWait

driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.amazon.com.mx/')
driver.implicitly_wait(10)


a_elements = driver.find_elements_by_xpath('//a')
for element in a_elements:
    print(element.text)


print('/////head/////')
head_elements = driver.find_elements_by_xpath('//head/*')
for element in head_elements:
    print(element.text)


print(len(a_elements))
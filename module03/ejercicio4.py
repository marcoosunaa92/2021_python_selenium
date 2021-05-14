from selenium.webdriver.common.keys import Keys

from common import get_driver
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.pinterest.com')
driver.find_element_by_xpath("//*[@data-test-id='simple-login-button']/button").click()
driver.find_element_by_id('email').send_keys('qamindstester@gmail.com')
driver.find_element_by_id('password').send_keys('Q@Minds4%<')
driver.find_element_by_xpath("//*[@data-test-id='registerFormSubmitButton']/button").click()


locator = (By.XPATH, "//*[contains(@data-test-id, 'search-box-input')]")
button_search = wait.until(EC.visibility_of_element_located(locator))
button_search.send_keys("Selenium")
button_search.send_keys(Keys.ENTER)

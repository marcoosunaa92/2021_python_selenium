from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.youtube.com/ ')


locator = (By.ID, 'search')
textfield_search = wait.until(EC.visibility_of_element_located(locator))
textfield_search.send_keys('Selenium')


locator = (By.ID, 'search-icon-legacy')
button_search = wait.until(EC.visibility_of_element_located(locator))
button_search.click()


locator = (By.ID, 'video-title')
link_video_name = wait.until(EC.visibility_of_all_elements_located(locator))
for video_titles in link_video_name:
    print(video_titles.text)


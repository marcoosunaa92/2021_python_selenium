from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')


driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://google.com')
print(driver.title)
print(driver.current_url)
print(driver.get_cookies())
print(driver.application_cache)
if 'Copyright The Closure Library Authors.' in driver.page_source:
    print('It exists')
else:
    print('Do not exist')
driver.quit()
# driver.get('https://www.mlb.com/es')
# print(driver.title)
# print(driver.current_url)
# driver.get('https://www.nytimes.com/es/')
# print(driver.title)
# print(driver.current_url)
# driver.back()
# driver.back()
# print(driver.title)
# print(driver.current_url)
# driver.quit()

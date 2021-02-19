from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')


def navigate_to_url(url_name):
    driver.find_element_by_link_text(url_name).click()
    print(driver.page_source.count('Selenium'))


driver = webdriver.Chrome(executable_path=get_chrome_path())

driver.get('https://www.selenium.dev/')
navigate_to_url('Downloads')
navigate_to_url('Projects')
navigate_to_url('Support')
navigate_to_url('Blog')




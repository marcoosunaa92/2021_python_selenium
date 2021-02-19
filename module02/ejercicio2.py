from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')


def func(driver2: webdriver, button_name: str):
    button_download = driver2.find_element_by_link_text(button_name)
    print(button_download.text)
    print(button_download.is_enabled())
    print(button_download.is_displayed())
    print(button_download.is_selected())


driver = webdriver.Chrome(executable_path=get_chrome_path())


driver.get('https://www.selenium.dev/')
print(driver.title)
print(driver.current_url)


func(driver, "Downloads")
func(driver, "Projects")
func(driver, "Support")
func(driver, "Blog")

driver.quit()
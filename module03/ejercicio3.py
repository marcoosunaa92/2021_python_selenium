from selenium.webdriver.remote.webelement import WebElement

from common import get_driver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


def dropdown(value: str):
    element = driver.find_element_by_class_name('p-dropdown__standings-view-dropdown-element')
    dropdown = Select(element)
    dropdown.select_by_visible_text(value)


def select_standard():
    driver.find_element_by_xpath("//*[contains(@class, 'standings-splits-button-group')]/div[1]").click()


def select_advanced():
    driver.find_element_by_xpath("//*[contains(@class, 'standings-splits-button-group')]/div[2]").click()


def team_info():
    rows = driver.find_elements_by_xpath('//*[@class="responsive-datatable__scrollable"]//tbody//tr')
    teams = []
    for row in rows:
        tmp = stat_info(row)
        teams.append(tmp)
    return teams


def stat_info(row: WebElement):
    stats = []
    for cell in row.find_elements_by_tag_name('td'):
        stats.append(cell.text)
    return stats


driver = get_driver('chrome')
wait = WebDriverWait(driver, 5)
driver.get('https://www.mlb.com/standings')
select_advanced()
dropdown('League')
teams = team_info()
for team in teams:
    print(' | '.join(team))
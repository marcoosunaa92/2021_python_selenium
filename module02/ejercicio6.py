from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select


driver = get_driver('chrome')
driver.get('https://formsmarts.com/form/axi?mode=h5')

FIRST_NAME = 'NameTEST'
LAST_NAME = 'LastTEST'
EMAIL = 'marco@anexinet.com'
ADDRESS = 'This address is a test message'
COUNTRY = 'AF'
DATE = '30/10/1992'
NUMBER_NIGHTS = 4


driver.find_element_by_id('u_LY9_60857').send_keys(FIRST_NAME)
driver.find_element_by_id('u_LY9_60858').send_keys(LAST_NAME)
driver.find_element_by_id('u_LY9_60859').send_keys(EMAIL)
driver.find_element_by_id('u_LY9_60860').send_keys(ADDRESS)
element = driver.find_element_by_id('u_LY9_60871')
dropdown = Select(element)
dropdown.select_by_value(COUNTRY)
driver.find_element_by_id('u_LY9_60861').clear()
driver.find_element_by_id('u_LY9_60861').send_keys(DATE)
driver.find_element_by_id('u_LY9_60866_0').click()
driver.find_element_by_id('u_LY9_60870').clear()
driver.find_element_by_id('u_LY9_60870').send_keys(NUMBER_NIGHTS)
driver.find_element_by_name('submit').click()


results = driver.find_elements_by_tag_name('td')
if results[0].text == FIRST_NAME:
    print('Name is correct.')
if results[1].text == LAST_NAME:
    print('Last name is correct.')
if results[2].text == EMAIL:
    print('Email is correct.')
if results[3].text == ADDRESS:
    print('Address is correct.')
if results[4].text == 'Afghanistan':
    print('Country is correct.')
if results[5].text == 'Friday October 30, 1992':
    print('Date is correct.')
if results[6].text == 'Double Room ($160 USD)':
    print('Room is correct.')
if results[7].text == str(NUMBER_NIGHTS):
    print('Number of nights is correct.')
else:
    print(results[7].text)

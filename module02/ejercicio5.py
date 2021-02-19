from common.webdriver_factory import get_driver
from selenium.webdriver.support.ui import Select


driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))
driver.find_element_by_id('u_k8f_4607').send_keys('Marco')
driver.find_element_by_id('u_k8f_338354').send_keys('Osuna')
driver.find_element_by_id('u_k8f_4608').send_keys('mosuna@anexinet.com')
element = driver.find_element_by_id('u_k8f_338367')
dropdown = Select(element)
dropdown.select_by_visible_text('Sales Inquiry')
driver.find_element_by_id('u_k8f_4609').send_keys('Hola Mundo')
driver.find_element_by_name('submit').click()
rows = driver.find_elements_by_tag_name('td')
if rows[0].text == 'Marco':
    print(f'El nombre "{rows[0].text}" es correcto.')
if rows[1].text == 'Osuna':
    print(f'El apellido "{rows[1].text}" es correcto.')
if rows[2].text == 'mosuna@anexinet.com':
    print(f'El email "{rows[2].text}" es correcto.')
if rows[3].text == 'Sales Inquiry':
    print(f'El dropdown "{rows[3].text}" es correcto.')
if rows[4].text == 'Hola Mundo':
    print(f'El comentario "{rows[4].text}" es correcto.')

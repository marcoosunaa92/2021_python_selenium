from common.webdriver_factory import get_driver

url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com' \
      '%2Fmail%2F&ltmpl=default&dsh=S-754881558%3A1613063574131574&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry' \
      '=SignUp '
driver = get_driver('chrome')
driver.get(url)

driver.find_element_by_id('firstName').send_keys('Marco')
driver.find_element_by_id('lastName').send_keys('Osuna')
driver.find_element_by_id('username').send_keys('osunamarco138')
driver.find_element_by_name('Passwd').send_keys('Tibia123|@#')
driver.find_element_by_name('ConfirmPasswd').send_keys('Tibia123|@#')
driver.find_element_by_class_name('VfPpkd-RLmnJb').click()
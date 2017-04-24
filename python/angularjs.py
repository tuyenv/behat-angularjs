import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#setting available
usr = "admin@example.com"
pwd = "secret"
archer_number = "Selenium Test"

#setup webdriver
delay = 30
sleep = 10
driver = webdriver.Firefox()
driver.get("http://localhost:8000/#/")
assert "Remediation Portal" in driver.title

try:
    #login with username/password
    element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "username")))
    elem = driver.find_element_by_id("username")
    elem.send_keys(usr)
    elem = driver.find_element_by_id("passwd")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "u-logout")))
    assert "incidents" in driver.current_url

    #select incident and click on View
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "check-incident-0"))).click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "selected-highlight"))).click()

    #process to assessment form
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-proceed"))).click()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-process"))).click()

    #process to create assessment
    elem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "archer-number")))
    elem.send_keys(archer_number)
    driver.find_element_by_css_selector("button[ng-click='vm.clickAddStakeholders()']").click()
    selectStakeholder = Select(driver.find_element_by_css_selector("select[ng-model='modalValue.stakeholderValue']"))
    selectStakeholder.select_by_index(1)


except Exception, e:
    print 'Exception: ' + str(e)

finally:
    print "OK"
    time.sleep(sleep)
    driver.quit()

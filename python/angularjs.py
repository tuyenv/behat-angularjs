import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#setting username and password
usr = "admin@example.com"
pwd = "secret"

#setup webdriver
delay = 15
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
    element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "u-logout")))
    assert "incidents" in driver.current_url
    WebDriverWait(driver, delay)

    #select incident and click on View
    driver.find_element_by_css_selector(".incidient-table tr td>input:first-child").click()
    WebDriverWait(driver, delay)
    driver.find_element_by_css_selector(".selected-highlight").click()
    WebDriverWait(driver, delay)

    #process to assessment form
    driver.find_element_by_css_selector(".btn-proceed").click()
    WebDriverWait(driver, delay)
    driver.find_element_by_css_selector(".confirm-process").click()

    #process to create assessment

except Exception, e:
    print 'Exception: ' + str(e)

finally:
    print "Finally!"
    time.sleep(5)
    driver.quit()

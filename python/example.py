from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

usr = "admin@example.com"
pwd = "secret"

driver = webdriver.Firefox()
driver.get("http://localhost:8000/#/")
assert "Remediation Portal" in driver.title

elem = driver.find_element_by_id("username")
elem.send_keys(usr)
elem = driver.find_element_by_id("passwd")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(driver.find_elements_by_css_selector('#u-logout')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"

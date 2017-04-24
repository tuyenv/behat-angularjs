import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RemediationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def testTitle(self):
        self.driver.get('http://localhost:8000/#/')
        self.assertEqual(self.driver.title, 'Remediation Portal')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

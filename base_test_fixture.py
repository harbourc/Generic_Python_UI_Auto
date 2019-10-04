from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class BaseTestFixture(unittest.TestCase):

    driver = None

    def setUp(self):
        print("Running SetUp")

        # declare chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("disable-infobars")

        # Start WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)

        # Call overriden _testInitialize in test case class
        self._testInitialize()

    def tearDown(self):
        print("Running Teardown")

        # Call overridden _testCleanup in test case class
        self._testCleanup

        self.driver.close()
        self.driver.quit()

    def _testInitialize(self):
        pass

    def _testCleanup(self):
        pass

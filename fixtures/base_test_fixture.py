from utils.driver_factory import DriverFactory
import unittest

class BaseTestFixture(unittest.TestCase):

    driver = None

    def setUp(self):
        print("Running SetUp")
        self.driver = DriverFactory.get_driver("chrome", headless=False)

        # Call overriden _testInitialize in test case class
        self._testInitialize()

    def tearDown(self):
        print("Running Teardown")

        # Call overridden _testCleanup in test case class
        self._testCleanup()

        if self.driver:
            self.driver.close()
            self.driver.quit()

    def _testInitialize(self):
        pass

    def _testCleanup(self):
        pass

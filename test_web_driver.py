import unittest
from base_test_fixture import BaseTestFixture
from google_home_page import GoogleHomePage


class TestGoogleSearch(BaseTestFixture):

    google_home_page = None

    def _testInitialize(self):

        # initialize google home page object
        self.google_home_page = GoogleHomePage(self.driver)

        # navigate to google url
        self.driver.get("https://www.google.com")

    def test_should_search_google(self):
        self.google_home_page.search("Python Tutorial")
        assert "Python Tutorial" in self.driver.title


if __name__ == '__main__':
    unittest.main()

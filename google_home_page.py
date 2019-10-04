from base_page_object import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleHomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):

        # wait for search input to exist
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Selectors.SEARCH_INPUT))

        # enter keyword in search bar
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ESCAPE)

        # click search button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.Selectors.SEARCH_BUTTON)).click()

        # wait until driver title contains the keyword
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(keyword))

    class Selectors(object):
        SEARCH_INPUT = (By.XPATH, "//input[@title='Search']")
        SEARCH_BUTTON = (By.XPATH, "//input[@value='Google Search']")

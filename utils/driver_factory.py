# driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:

    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        driver = None
        if browser_name.lower() == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("disable-infobars")
            if headless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=chrome_options)
        elif browser_name.lower() == "firefox":
            raise NotImplementedError(f"Browser '{browser_name}' not yet implemented.")
        else:
            raise ValueError(f"Unsupported browser: {browser_name}. Please choose 'chrome' or 'firefox'.")

        return driver
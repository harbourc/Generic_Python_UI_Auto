class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

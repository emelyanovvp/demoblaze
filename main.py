

class Main:
    def __init__(self, driver, url, timeout):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(5)

    def open(self):
        self.driver.get(self.url)
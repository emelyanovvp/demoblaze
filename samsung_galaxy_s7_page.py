import time

from .main import Main
from .locators import SamsungGalaxyS7Locators
from .cart_page import CartPage


class SamsungGalaxyS7Page(Main):
    def add_samsung_galaxy_s7_to_cart(self):
        self.driver.find_element(*SamsungGalaxyS7Locators.ADD_TO_CART_BUTTON).click()
        time.sleep(2)

    def go_to_cart_page(self):
        self.driver.find_element(*SamsungGalaxyS7Locators.CART_BUTTON).click()
        time.sleep(2)
        return CartPage(driver=self.driver, url=self.driver.current_url, timeout=10)


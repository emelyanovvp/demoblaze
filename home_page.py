from .main import Main
from .locators import HomePageLocators
from .cart_page import CartPage
from .samsung_galaxy_s7_page import SamsungGalaxyS7Page
import time


class HomePage(Main):
    def go_to_cart_page(self):
        self.driver.find_element(*HomePageLocators.CART_BUTTON).click()
        return CartPage(driver=self.driver, url=self.driver.current_url, timeout=10)

    def go_to_samsung_galaxy_s7_page(self):
        self.driver.find_element(*HomePageLocators.PHONES_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*HomePageLocators.SAMSUNG_GALAXY_S7_LINK).click()
        time.sleep(2)
        return SamsungGalaxyS7Page(driver=self.driver, url=self.driver.current_url, timeout=5)
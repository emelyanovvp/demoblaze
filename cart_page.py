from .main import Main
from .locators import CartPageLocators
import time


class CartPage(Main):
    def click_place_order_button(self):
        self.driver.find_element(*CartPageLocators.PLACE_ORDER_BUTTON).click()







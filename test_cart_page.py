import pytest
import time
from .cart_page import CartPage
from .locators import CartPageLocators


def test_place_order_and_purchase(driver):
    url = "https://www.demoblaze.com/cart.html"
    page_cart = CartPage(driver, url, timeout=5)
    page_cart.open()
    page_cart.click_place_order_button()
    time.sleep(3)
    for handle in driver.window_handles:
        if handle != page_cart:
            popup_window = handle
            driver.switch_to.window(popup_window)
            driver.find_element(*CartPageLocators.INPUT_NAME_BLANK).send_keys("Greg")
            driver.find_element(*CartPageLocators.INPUT_COUNTRY_BLANK).send_keys("USA")
            driver.find_element(*CartPageLocators.INPUT_CITY_BLANK).send_keys("Chicago")
            driver.find_element(*CartPageLocators.INPUT_CARD_BLANK).send_keys("123456789")
            driver.find_element(*CartPageLocators.INPUT_MONTH_BLANK).send_keys("12")
            driver.find_element(*CartPageLocators.INPUT_YEAR_BLANK).send_keys("2022")
            driver.find_element(*CartPageLocators.PURCHASE_BUTTON).click()
            time.sleep(2)

    for h in driver.window_handles:
        if h != page_cart:
            thanks_window = h
            driver.switch_to.window(thanks_window)
            thanks_element = driver.find_element(*CartPageLocators.THANKS_MESSAGE)
            thanks_text = thanks_element.text
            assert thanks_text == "Thank you for your purchase!", "No purchases were done"


def test_try_purchase_without_placing_order(driver):
    url = "https://www.demoblaze.com/cart.html"
    page_cart = CartPage(driver, url, timeout=5)
    page_cart.open()
    page_cart.click_place_order_button()
    time.sleep(3)
    for handle in driver.window_handles:
        if handle != page_cart:
            popup_window = handle
            driver.switch_to.window(popup_window)
            driver.find_element(*CartPageLocators.PURCHASE_BUTTON).click()
            time.sleep(2)
            alert_window = driver.switch_to.alert
            alert_text = alert_window.text
            alert_window.accept()
            assert alert_text == "Please fill out Name and Creditcard."


if __name__ == '__main__':
    pytest.main()
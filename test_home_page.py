import pytest
from .home_page import HomePage
from .locators import SignUpLocators
import time

def test_go_to_cart_page(driver):
    url = "https://www.demoblaze.com/index.html"
    page = HomePage(driver, url, timeout=5)
    page.open()
    page.go_to_cart_page()
    assert "cart" in driver.current_url, "Cart page is not presented"


def test_go_to_samsung_galaxy_s7_page(driver):
    url = "https://www.demoblaze.com/index.html"
    page = HomePage(driver, url, timeout=5)
    page.open()
    page.go_to_samsung_galaxy_s7_page()
    assert "idp_=4" in driver.current_url, "No such type of page"


def test_sign_up(driver):
    url = "https://www.demoblaze.com/index.html"
    home_page = HomePage(driver, url, timeout=5)
    home_page.open()
    home_page.sign_up()
    for handle in driver.window_handles:
        if handle != home_page:
            log_in_window = handle
            driver.switch_to.window(log_in_window)
            driver.find_element(*SignUpLocators.INPUT_USERNAME_BLANK).send_keys("Olga")
            driver.find_element(*SignUpLocators.INPUT_PASSWORD_BLANK).send_keys("123456")
            driver.find_element(*SignUpLocators.SIGN_UP_BUTTON).click()
            time.sleep(2)
            alert_window = driver.switch_to.alert
            alert_text = alert_window.text
            alert_window.accept()
            assert alert_text == "Sign up successful.", "This user already exist."


if __name__ == '__main__':
    pytest.main()
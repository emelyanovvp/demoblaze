import time
import pytest
from .samsung_galaxy_s7_page import SamsungGalaxyS7Page
from .cart_page import CartPage


def test_add_samsung_galaxy_s7_to_cart(driver):
    url = "https://www.demoblaze.com/prod.html?idp_=4#"
    page = SamsungGalaxyS7Page(driver, url, timeout=2)
    page.open()
    page.add_samsung_galaxy_s7_to_cart()
    time.sleep(2)
    alert = driver.switch_to.alert
    text = alert.text
    assert text == "Product added", "Product wasn't added"

def test_go_to_cart_page(driver):
    url = "https://www.demoblaze.com/prod.html?idp_=4#"
    page = SamsungGalaxyS7Page(driver, url, timeout=5)
    page.open()
    page.go_to_cart_page()
    assert "cart" in driver.current_url, "Cart page is not presented"


if __name__ == '__main__':
    pytest.main()
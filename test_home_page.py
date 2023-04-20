import pytest
from .home_page import HomePage


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


if __name__ == '__main__':
    pytest.main()
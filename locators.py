from selenium.webdriver.common.by import By


class HomePageLocators:
    SAMSUNG_GALAXY_S7_LINK = (By.XPATH, "//a[text()='Samsung galaxy s7']")
    HOME_BUTTON = (By.XPATH, "//a[text()='Home ']")
    CONTACT_BUTTON = (By.XPATH, "//a[text()='Contact']")
    ABOUT_US_BUTTON = (By.XPATH, "//a[text()='About us']")
    CART_BUTTON = (By.XPATH, "//a[text()='Cart']")
    LOG_IN_BUTTON = (By.XPATH, "//a[text()='Log in']")
    SIGN_UP_BUTTON = (By.XPATH, "//a[text()='Sign up']")
    PHONES_BUTTON = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS_BUTTON = (By.XPATH, "//a[text()='Laptops']")
    MONITORS_BUTTON = (By.XPATH, "//a[text()='Monitors']")

class SamsungGalaxyS7Locators:
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text()='Add to cart']")
    CART_BUTTON = (By.XPATH, "//a[text()='Cart']")


class CartPageLocators:
    THANKS_MESSAGE = (By.XPATH, "//h2[text()='Thank you for your purchase!']")

    PLACE_ORDER_TITLE = (By.XPATH, "//h5[text()='Place order']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Place Order']")
    INPUT_NAME_BLANK = (By.CSS_SELECTOR, "input#name")
    INPUT_COUNTRY_BLANK =(By.CSS_SELECTOR, "input#country")
    INPUT_CITY_BLANK = (By.CSS_SELECTOR, "input#city")
    INPUT_CARD_BLANK = (By.CSS_SELECTOR, "input#card")
    INPUT_MONTH_BLANK = (By.CSS_SELECTOR, "input#month")
    INPUT_YEAR_BLANK = (By.CSS_SELECTOR, "input#year")
    PURCHASE_BUTTON = (By.XPATH, "//button[text()='Purchase']")
    CLOSE_BUTTON = (By.XPATH, "//button[text()='Close']")



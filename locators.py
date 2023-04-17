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

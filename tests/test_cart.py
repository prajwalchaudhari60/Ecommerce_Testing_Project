from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import time

def test_add_to_cart():

    # Open browser
    driver = webdriver.Chrome()

    # Open website
    driver.get("https://www.saucedemo.com")

    # Create LoginPage object
    login = LoginPage(driver)

    # Enter username
    login.enter_username("standard_user")

    # Enter password
    login.enter_password("secret_sauce")

    # Click login
    login.click_login()

    # Create CartPage object
    cart = CartPage(driver)

    # Add product to cart
    cart.add_product_to_cart()

    # Open cart
    cart.open_cart()

    # Verification
    assert "cart" in driver.current_url

    # Screenshot
    driver.save_screenshot("screenshots/cart_test.png")

    time.sleep(3)

    # Close browser
    driver.quit()
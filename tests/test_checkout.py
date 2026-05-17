from selenium import webdriver
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

def test_checkout():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    cart = CartPage(driver)

    cart.add_product_to_cart()
    cart.open_cart()

    checkout = CheckoutPage(driver)

    checkout.click_checkout()

    checkout.enter_first_name("Prajwal")
    checkout.enter_last_name("Chaudhari")
    checkout.enter_zipcode("413512")

    checkout.click_continue()

    checkout.click_finish()

    assert "checkout-complete" in driver.current_url

    driver.save_screenshot("screenshots/checkout.png")

    time.sleep(3)

    driver.quit()
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
import time

def test_logout():

    driver = webdriver.Chrome()
    

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    logout = LogoutPage(driver)

    logout.open_menu()

    time.sleep(2)

    logout.click_logout()

    assert "saucedemo" in driver.current_url

    driver.save_screenshot("screenshots/logout.png")

    time.sleep(3)

    driver.quit()
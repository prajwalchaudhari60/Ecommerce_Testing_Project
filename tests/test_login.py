from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_login():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url

    driver.save_screenshot("screenshots/login.png")

    time.sleep(3)

    driver.quit()
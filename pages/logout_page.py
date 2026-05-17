from selenium.webdriver.common.by import By

class LogoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.menu_button = (By.ID, "react-burger-menu-btn")

        self.logout_link = (By.ID, "logout_sidebar_link")

    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_link).click()
from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.checkout_button = (By.ID, "checkout")

        self.first_name = (By.ID, "first-name")

        self.last_name = (By.ID, "last-name")

        self.zip_code = (By.ID, "postal-code")

        self.continue_button = (By.ID, "continue")

        self.finish_button = (By.ID, "finish")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_first_name(self, fname):
        self.driver.find_element(*self.first_name).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(*self.last_name).send_keys(lname)

    def enter_zipcode(self, zip):
        self.driver.find_element(*self.zip_code).send_keys(zip)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
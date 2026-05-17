from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

        # Locator for Add to Cart button
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")

        # Locator for cart icon
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    # Method to click Add to Cart
    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    # Method to open cart
    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
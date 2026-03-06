from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        xpath = (f"//div[text()='{item_name}']/ancestor::"
                 f"div[@class='inventory_item']//button")
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_text = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
        return total_text.split(": ")[1]

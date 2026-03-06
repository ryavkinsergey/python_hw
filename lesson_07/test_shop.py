from selenium import webdriver
from shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


def test_saucedemo_purchase():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Ivan", "Ivanov", "123456")

    total = checkout.get_total_price()

    driver.quit()
    assert total == "$58.29"

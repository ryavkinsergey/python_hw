import allure
from selenium import webdriver
from shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


@allure.epic("ДЗ №10")
@allure.feature("Магазин")
@allure.story("Покупка товаров")
@allure.title("Тест оформления заказа в SauceDemo")
@allure.description("Сквозной сценарий: от логина до проверки итоговой суммы")
@allure.severity(allure.severity_level.CRITICAL)
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

    with allure.step("Проверить итоговую стоимость заказа"):
        total = checkout.get_total_price()
        assert total == "$58.29"  # Исправил на реальную сумму из корзины

    driver.quit()

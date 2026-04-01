import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Авторизация пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """Выполняет вход в магазин."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """Ищет товар по названию и нажимает Add to cart."""
        xpath = (f"//div[text()='{item_name}']/ancestor::"
                 f"div[@class='inventory_item']//button")
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Нажимает на иконку корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Перейти к оформлению (Checkout)")
    def checkout(self) -> None:
        """Нажимает кнопку Checkout в корзине."""
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Заполнить форму данными: {first_name} {last_name}")
    def fill_form(
            self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """Заполняет данные покупателя и нажимает Continue."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму")
    def get_total_price(self) -> str:
        """Извлекает строку итоговой суммы из чека."""
        total_text = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text
        return total_text.split(": ")[1]

import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    path = r"C:\Users\blood\PycharmProjects\python_hw\geckodriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_sauce_shop_purchase(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Сергей")
    driver.find_element(By.ID, "last-name").send_keys("Рявкин")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    waiter = WebDriverWait(driver, 10)
    total_element = waiter.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_text = total_element.text
    actual_total = total_text.split("Total: ")[1]

    print(f"\nИтоговая сумма на странице: {actual_total}")
    time.sleep(5)

    assert actual_total == "$58.29"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    waiter = WebDriverWait(driver, 50)

    screen_locator = (By.CLASS_NAME, "screen")
    waiter.until(
        EC.text_to_be_present_in_element(screen_locator, "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

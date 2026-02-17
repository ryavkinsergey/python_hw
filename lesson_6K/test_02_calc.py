import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    path = (
        r"C:\Users\blood\PycharmProjects\python_hw"
        r"\chromedriver-win64\chromedriver.exe"
    )
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
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

    waiter.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15"

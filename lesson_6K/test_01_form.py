import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    path = (
        r"C:\Users\blood\PycharmProjects\python_hw"
        r"\edgedriver_win64\msedgedriver.exe"
    )
    service = Service(executable_path=path)
    driver = webdriver.Edge(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_form_validation(driver):
    # Выносим URL в переменную и разбиваем для соблюдения лимита в 79 символов
    url = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )
    driver.get(url)

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 10)
    zip_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    assert "alert-danger" in zip_field.get_attribute("class")

    # Переносим элементы списка на новые строки (E501)
    success_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in success_fields:
        field_class = driver.find_element(
            By.ID, field_id
        ).get_attribute("class")
        assert "alert-success" in field_class

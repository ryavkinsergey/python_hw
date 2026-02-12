from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\blood\PycharmProjects\python_hw\geckodriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service)

driver.implicitly_wait(10)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    success_message = driver.find_element(By.ID, "flash").text
    print(f"Текст уведомления: {success_message}")

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

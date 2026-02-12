from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = r"C:\Users\blood\PycharmProjects\python_hw\geckodriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("Sky")
    time.sleep(2)

    input_field.clear()
    time.sleep(1)

    input_field.send_keys("Pro")
    time.sleep(2)

    print("Скрипт успешно выполнен в Firefox")

except Exception as ex:
    print(f"Ошибка при выполнении: {ex}")

finally:
    driver.quit()

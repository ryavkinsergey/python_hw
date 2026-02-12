from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\blood\PycharmProjects\python_hw\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    dynamic_button = driver.find_element(
        By.XPATH, "//button[text()='Button with Dynamic ID']"
    )
    dynamic_button.click()

    print("Кнопка успешно нажата")

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

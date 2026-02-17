from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = (
    r"C:\Users\blood\PycharmProjects\python_hw"
    r"\chromedriver-win64\chromedriver.exe"
)

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()

    print(blue_button.text)

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

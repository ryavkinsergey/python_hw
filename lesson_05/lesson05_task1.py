from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = (
    r"C:\Users\blood\PycharmProjects\python_hw"
    r"\chromedriver-win64\chromedriver.exe"
)
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(10)

try:
    driver.get("http://uitestingplayground.com/classattr")

    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    alert = driver.switch_to.alert
    print(f"Текст уведомления: {alert.text}")
    alert.accept()

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

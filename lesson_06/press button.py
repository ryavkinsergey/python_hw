from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = (
    r"C:\Users\blood\PycharmProjects\python_hw"
    r"\chromedriver-win64\chromedriver.exe"
)

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/ajax")

    driver.find_element(By.ID, "ajaxButton").click()

    waiter = WebDriverWait(driver, 20)
    success_banner = waiter.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    print(success_banner.text)

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

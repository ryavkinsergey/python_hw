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
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    waiter = WebDriverWait(driver, 30)
    waiter.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#image-container img:nth-child(4)")
        )
    )

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_image_src = images[2].get_attribute("src")

    print(third_image_src)

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

finally:
    driver.quit()

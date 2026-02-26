from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 55)
        self.delay_input = (By.ID, "delay")
        self.result_screen = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, text):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    def get_result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text

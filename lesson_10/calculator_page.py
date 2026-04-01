import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 55)
        self._delay_input = (By.ID, "delay")
        self._result_screen = (By.CLASS_NAME, "screen")

    @allure.step("Установить задержку {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """Устанавливает время задержки в поле ввода."""
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать на кнопку '{text}'")
    def click_button(self, text: str) -> None:
        """Находит и нажимает кнопку калькулятора по тексту."""
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    @allure.step("Ожидание и получение результата")
    def get_result(self) -> str:
        """Дожидается появления результата '15' и возвращает текст экрана."""
        self.wait.until(
            EC.text_to_be_present_in_element(self._result_screen, "15")
        )
        return self.driver.find_element(*self._result_screen).text

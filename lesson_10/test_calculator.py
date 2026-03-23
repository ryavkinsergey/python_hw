import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.epic("ДЗ №10")
@allure.feature("Калькулятор")
@allure.story("Ожидание результата")
@allure.title("Тест медленного калькулятора")
@allure.description("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calc():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/slow-calculator.html")

    page = CalculatorPage(driver)
    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    with allure.step("Проверить, что итоговая сумма равна 15"):
        assert page.get_result() == "15"

    driver.quit()

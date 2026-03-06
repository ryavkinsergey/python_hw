from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calc():
    driver = webdriver.Chrome()
    url = ("https://bonigarcia.dev/"
           "selenium-webdriver-java/slow-calculator.html")
    driver.get(url)

    page = CalculatorPage(driver)
    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    assert page.get_result() == "15"
    driver.quit()

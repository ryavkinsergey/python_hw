# Lesson 10: Allure Reports & Type Hinting

## Как запустить тесты
1. Установите зависимости:
   `pip install pytest allure-pytest selenium`
2. Выполните запуск:
   `pytest --alluredir=allure-results lesson_10/`

## Как просмотреть отчет
1. Если установлен Allure CLI:
   `allure serve allure-results`
2. Если нужно просто сгенерировать папку с отчетом:
   `allure generate allure-results -o allure-report`

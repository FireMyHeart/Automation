import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPageTwo import MainPageTwo
import allure


@allure.id("LSN10-2")
@allure.epic("Тесты UI. Практика ввода данных в поля")
@allure.story("Форма Slow calculator")
@allure.feature("Calculate")
@allure.title("Сложение двух чисел")
@allure.description("Сложение двух целых положительных однозначных чисел")
@allure.severity("critical")
@allure.suite("UI тесты практика")
@pytest.mark.parametrize('num1, num2, result', [(7, 8, 15)])
def test_step_two_1(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(7, 8, '+')

    assert res == result
    driver.quit()


@allure.id("LSN10-3")
@allure.epic("Тесты UI. Практика ввода данных в поля")
@allure.story("Форма Slow calculator")
@allure.feature("Calculate")
@allure.title("Вычитание двух чисел")
@allure.description("Вычитание двух целых положительных однозначных чисел")
@allure.severity("critical")
@allure.suite("UI тесты практика")
@pytest.mark.parametrize('num1, num2, result', [(9, 3, 6)])
def test_step_two_2(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(9, 3, '-')

    assert res == result
    driver.quit()


@allure.id("LSN10-4")
@allure.epic("Тесты UI. Практика ввода данных в поля")
@allure.story("Форма Slow calculator")
@allure.feature("Calculate")
@allure.title("Деление двух чисел")
@allure.description("Целочисленное деление двух положительных целых однозначных чисел")
@allure.severity("critical")
@allure.suite("UI тесты практика")
@pytest.mark.parametrize('num1, num2, result', [(8, 4, 2)])
def test_step_two_3(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(8, 4, '÷')

    assert res == result
    driver.quit()


@allure.id("LSN10-5")
@allure.epic("Тесты UI. Практика ввода данных в поля")
@allure.story("Форма Slow calculator")
@allure.feature("Calculate")
@allure.title("Умножение двух чисел")
@allure.description("Умножение двух целых положительных однозначных чисел")
@allure.severity("critical")
@allure.suite("UI тесты практика")
@pytest.mark.parametrize('num1, num2, result', [(2, 3, 6)])
def test_step_two_4(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(2, 3, 'x')

    assert res == result
    driver.quit()

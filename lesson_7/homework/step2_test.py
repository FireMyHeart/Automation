import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPageTwo import MainPageTwo

@pytest.mark.parametrize('num1, num2, result', [(7, 8, 15)])
def test_step_two_1(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(7, 8, '+')
    
    assert res == result
    driver.quit()

@pytest.mark.parametrize('num1, num2, result', [(9, 3, 6)])
def test_step_two_2(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(9, 3, '-')
    
    assert res == result
    driver.quit()

@pytest.mark.parametrize('num1, num2, result', [(9, 3, 3)])
def test_step_two_3(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(9, 3, '÷')
    
    assert res == result
    driver.quit()

@pytest.mark.parametrize('num1, num2, result', [(2, 3, 6)])
def test_step_two_4(num1, num2, result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageTwo(driver)
    main_page.enter_time('1')
    res = main_page.calculate(2, 3, 'x')
    
    assert res == result
    driver.quit()

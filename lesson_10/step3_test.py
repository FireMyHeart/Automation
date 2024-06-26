import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPageThree import MainPageThree
import allure


@allure.id("LSN10-6")
@allure.epic("Тесты UI. Практика ввода данных в поля")
@allure.story("Сайт Swag Labs")
@allure.feature("Total sum")
@allure.title("Добавление в корзину трех товаров")
@allure.description("Добавление в корзину трех товаров авторизованным пользователем и проверка итоговой суммы покупки")
@allure.severity("major")
@allure.suite("UI тесты практика")
@pytest.mark.parametrize('result', [('58.29')])
def test_step_two(result: str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageThree(driver)
    main_page.auth()
    main_page.add_to_cart()
    main_page.checkout('Аня', 'Котикова', '214013')
    res = main_page.summary()
    assert res == result
    driver.quit()

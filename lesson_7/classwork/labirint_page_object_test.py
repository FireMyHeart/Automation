from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

def test_cart_counter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search('Python')

    result_page = ResultPage(driver)
    to_be = result_page.add_to_cart()

    cart_page = CartPage(driver)
    cart_page.get()
    current_result = cart_page.get_counter()
    assert to_be == current_result
    driver.quit()

def test_empty_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search('no book search term')
    result_page = ResultPage(driver)
    message = result_page.get_empty_result_message()
    assert message == 'Мы ничего не нашли по вашему запросу! Что делать?'
    driver.quit()

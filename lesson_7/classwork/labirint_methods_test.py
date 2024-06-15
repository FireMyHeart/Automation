from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def open_labirint():
    # перейти на сайт лабиринта
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.add_cookie(cookie)

def search(phrase):
    # найти все книги по слову Python
    driver.find_element(By.ID, 'search-field').send_keys(phrase)
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

def add_to_cart():
    # добавить все книги в корзину
    buy_buttons = driver.find_elements(
        By.CSS_SELECTOR, 'a._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return str(counter)

def go_to_cart():
    # перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    # проверить счетчик товаров. Должен быть равен числу нажатий
    # получить текущее значение
    txt = driver.find_element(By.XPATH, '//*[@id="ui-id-4"]/b').text
    return txt

def close():
    driver.quit()

def get_title():
    txt = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/h1').text
    return txt

def test_cart_counter():
    open_labirint()
    search('Python')
    added = add_to_cart()
    go_to_cart()
    result = get_cart_counter()
    close()
    # сравнить с counter
    assert added == result

def test_empty_search():
    open_labirint()
    search('no book search term')
    result = get_title()
    assert result == 'Мы ничего не нашли по вашему запросу! Что делать?'

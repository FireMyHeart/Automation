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

def test_cart_counter():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # перейти на сайт лабиринта
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.add_cookie(cookie)
    # найти все книги по слову Python
    driver.find_element(By.ID, 'search-field').send_keys('Python')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    # добавить все книги в корзину
    buy_buttons = driver.find_elements(
        By.CSS_SELECTOR, 'a._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1

    # перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

    # проверить счетчик товаров. Должен быть равен числу нажатий
    # получить текущее значение
    txt = driver.find_element(By.XPATH, '//*[@id="ui-id-4"]/b').text

    # сравнить с counter
    assert str(counter) == txt
    driver.quit()

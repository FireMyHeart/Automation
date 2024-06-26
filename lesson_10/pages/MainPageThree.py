from selenium.webdriver.common.by import By
import allure


class MainPageThree:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)

    @allure.step("Авторизоваться на сайте")
    def auth(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    
    @allure.step("Добавить в корзину три товара и перейти в корзину")
    def add_to_cart(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-onesie"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    @allure.step("Ввести данные для доставки: имя {fname}, фамилию {lname}, индекс {index}")
    def checkout(self, fname: str, lname: str, index: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys(fname)
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys(lname)
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys(index)
    
    @allure.step("Вернуть итоговую сумму покупки")
    def summary(self) -> str:
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total[8:]

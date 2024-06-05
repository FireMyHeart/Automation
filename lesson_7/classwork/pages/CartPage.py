from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self._driver = driver
    
    def get(self):
        self._driver.get("https://www.labirint.ru/cart/")
    
    def get_counter(self):
        txt = self._driver.find_element(By.XPATH, '//*[@id="ui-id-4"]/b').text
        return txt

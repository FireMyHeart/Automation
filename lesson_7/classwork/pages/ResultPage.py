from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self):
        buy_buttons = self._driver.find_elements(
            By.CSS_SELECTOR, 'a._btn.btn-tocart.buy-link')
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return str(counter)
    
    def get_empty_result_message(self):
        txt = self._driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/h1').text
        return txt

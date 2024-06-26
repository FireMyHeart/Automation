from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageTwo:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)

    def enter_time(self, sec):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(sec)
    
    def calculate(self, a, b, sign):
        term1 = "//span[text()='" + str(a) + "']"
        self._driver.find_element(By.XPATH, term1).click()
        operation = "//span[text()='" + sign + "']"
        self._driver.find_element(By.XPATH, operation).click()

        term2 = "//span[text()='" + str(b) + "']"
        self._driver.find_element(By.XPATH, term2).click()

        res = self._driver.find_element(By.XPATH, "//span[text()='=']")
        res.click()

        waiter = WebDriverWait(self._driver, 60)
        if sign == '+':
            waiter.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(a + b))
            )
        elif sign == '-':
            waiter.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(a - b))
            )
        elif sign == 'x':
            waiter.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(a * b))
            )
        elif sign == '÷':
            waiter.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(int(a / b)))
            )
        return int(self._driver.find_element(By.CSS_SELECTOR, '.screen').text)

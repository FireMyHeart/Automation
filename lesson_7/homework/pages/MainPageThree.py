from selenium.webdriver.common.by import By

class MainPageThree:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)

    def auth(self):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    
    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-onesie"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    def checkout(self, fname, lname, index):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        self._driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys(fname)
        self._driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys(lname)
        self._driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys(index)
    
    def summary(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total[8:]

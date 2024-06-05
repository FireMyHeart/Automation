from selenium.webdriver.common.by import By

class MainPageOne:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    def enter_values(self, css_name, key):
        self._driver.find_element(By.CSS_SELECTOR, f'input[name="{css_name}"]').send_keys(key)
    
    def clicker(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    def bg_color(self, css_name):
        return self._driver.find_element(By.ID, css_name).value_of_css_property("background-color")

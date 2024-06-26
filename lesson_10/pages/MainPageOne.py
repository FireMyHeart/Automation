from selenium.webdriver.common.by import By
import allure


class MainPageOne:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)

    @allure.step("Ввести в поле {css_name} значение {key}")
    def enter_values(self, css_name: str, key: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, f'input[name="{css_name}"]').send_keys(key)

    @allure.step("Нажать кнопку Submit")
    def clicker(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step("Вернуть код цвета бэкграунда в поле {css_name}")
    def bg_color(self, css_name: str) -> str:
        return self._driver.find_element(By.ID, css_name).value_of_css_property("background-color")

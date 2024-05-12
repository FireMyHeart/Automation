from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

input_username = driver.find_element(By.CSS_SELECTOR, 'input#username')
input_username.send_keys("tomsmith")
input_password = driver.find_element(By.CSS_SELECTOR, 'input#password')
input_password.send_keys("SuperSecretPassword!")
button_login = driver.find_element(By.CSS_SELECTOR, 'button')
button_login.click()

try:
    alert = driver.switch_to.alert
    alert.accept()  # Нажать Ok в модальном окне алерт
except:
    pass

sleep(5)

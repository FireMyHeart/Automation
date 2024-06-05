from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(a, b):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("5")
    term1 = "//span[text()='" + str(a) + "']"
    element_7 = driver.find_element(By.XPATH, term1)
    element_7.click()
    element_plus = driver.find_element(By.XPATH, "//span[text()='+']")
    element_plus.click()
    term2 = "//span[text()='" + str(b) + "']"
    element_8 = driver.find_element(By.XPATH, term2)
    element_8.click()
    element_result = driver.find_element(By.XPATH, "//span[text()='=']")
    element_result.click()
    waiter = WebDriverWait(driver, 60)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(a + b))
    )
    return int(driver.find_element(By.CSS_SELECTOR, '.screen').text)

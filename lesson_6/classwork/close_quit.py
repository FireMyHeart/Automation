from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.CSS_SELECTOR, 'button#tabButton').click()
sleep(3)
driver.close()
sleep(5)
driver.quit()
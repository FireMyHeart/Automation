from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://labirint.ru")

element = driver.find_element(By.CSS_SELECTOR, '#search-field')
element.clear()
element.send_keys('Аня Доброчасова')
# element.click()
driver.find_element(By.CSS_SELECTOR, '.b-header-b-search-e-btn').click()

# print(element)
sleep(10)
driver.quit()
#driver.find_elements()


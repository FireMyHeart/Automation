from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    # почему только в цикле работает? Ведь поиск не по id. Или все равно в ячейку памяти сохраняется id элемента, как бы я его ни искала?
    button.click()
    driver.refresh()

sleep(5)
driver.quit()

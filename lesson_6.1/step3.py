from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user", Keys.TAB)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-onesie"]').click()

    driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys("Аня")
    driver.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys("Краева")
    driver.find_element(By.CSS_SELECTOR, 'input#postal-code').send_keys("214013")

    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    #total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/text()[2]').text
    total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    return total[8:]

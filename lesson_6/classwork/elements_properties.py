from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://labirint.ru")
# txt = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').text
# print(txt)
# 
# tag = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').tag_name
# print(tag)
# 
# id = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').id
# print(id)
# 
# href = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').get_attribute('href')
# print(href)
# 
# ff = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').value_of_css_property('font-family')
# print(ff)
# 
# color = driver.find_element(By.CSS_SELECTOR, 'li[data-toggle="header-office"]').value_of_css_property('color')
# print(color)

# driver.get("http://uitestingplayground.com/visibility")
# is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)
# 
# driver.find_element(By.CSS_SELECTOR, '#hideButton').click()
# 
# is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# print(is_displayed)
# 
# sleep(2)

# driver.get("https://demoqa.com/radio-button")
# is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
# print(is_enabled)
# 
# is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
# print(is_enabled)
# 
# driver.quit()

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# cb = driver.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
# is_selected = cb.is_selected()
# print(is_selected)
# cb.click()
# is_selected = cb.is_selected()
# print(is_selected)
# sleep(2)
# driver.quit()

driver.get("https://the-internet.herokuapp.com/checkboxes")
# div = driver.find_element(By.CSS_SELECTOR, '#page-footer')
# a = div.find_element(By.CSS_SELECTOR, 'a')
# print(a.get_attribute('href'))
inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
print(len(inputs))
input1 = inputs[1]
print(input1.get_attribute('type'))
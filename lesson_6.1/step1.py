from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def check_bg():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com",)
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    bg_zipcode = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
    bg_fname = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color")
    bg_lname = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color")
    bg_address = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("background-color")
    bg_city = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
    bg_country = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("background-color")
    bg_email = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
    bg_phone = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
    bg_jobposition = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color")
    bg_company = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property("background-color")

    return [bg_zipcode == 'rgba(248, 215, 218, 1)', bg_fname == 'rgba(209, 231, 221, 1)', bg_lname == 'rgba(209, 231, 221, 1)', bg_address == 'rgba(209, 231, 221, 1)', bg_city == 'rgba(209, 231, 221, 1)', bg_country == 'rgba(209, 231, 221, 1)', bg_email == 'rgba(209, 231, 221, 1)', bg_phone == 'rgba(209, 231, 221, 1)', bg_jobposition == 'rgba(209, 231, 221, 1)', bg_company == 'rgba(209, 231, 221, 1)']

#alert = driver.switch_to.alert
#alert.dismiss()
#driver.switch_to.default_content()
#assert 'rgba(248, 215, 218, 1)' in driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
# assert "rgba(209, 231, 221, 1)" in driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color")
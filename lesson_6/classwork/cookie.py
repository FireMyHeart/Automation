# from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("http://labirint.ru")
driver.add_cookie(cookie)

cookie1 = driver.get_cookie('PHPSESSID')
cookies = driver.get_cookies()
print(cookies)

# driver.refresh()
# driver.delete_all_cookies()
# sleep(10)
driver.quit()
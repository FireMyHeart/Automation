import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPageThree import MainPageThree

@pytest.mark.parametrize('result', [('58.29')])
def test_step_two(result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageThree(driver)
    main_page.auth()
    main_page.add_to_cart()
    main_page.checkout('Аня', 'Котикова', '214013')
    res = main_page.summary()
    assert res == result
    driver.quit()

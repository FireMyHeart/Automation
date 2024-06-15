import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPageOne import MainPageOne

@pytest.mark.parametrize('result', [([True, True, True, True, True, True, True, True, True, True])])
def test_step_one(result):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPageOne(driver)

    main_page.enter_values("first-name", "Иван")
    main_page.enter_values("last-name", "Петров")
    main_page.enter_values("address", "Ленина, 55-3")
    main_page.enter_values("city", "Москва")
    main_page.enter_values("country", "Россия")
    main_page.enter_values("e-mail", "test@skypro.com")
    main_page.enter_values("phone", "+7985899998787")
    main_page.enter_values("job-position", "QA")
    main_page.enter_values("company", "SkyPro")
    main_page.clicker()
    bg_zipcode = main_page.bg_color("zip-code")
    bg_fname = main_page.bg_color("first-name")
    bg_lname = main_page.bg_color("last-name")
    bg_address = main_page.bg_color("address")
    bg_city = main_page.bg_color("city")
    bg_country = main_page.bg_color("country")
    bg_email = main_page.bg_color("e-mail")
    bg_phone = main_page.bg_color("phone")
    bg_jobposition = main_page.bg_color("job-position")
    bg_company = main_page.bg_color("company")
    assert result == [bg_zipcode == 'rgba(248, 215, 218, 1)',
                    bg_fname == 'rgba(209, 231, 221, 1)',
                    bg_lname == 'rgba(209, 231, 221, 1)',
                    bg_address == 'rgba(209, 231, 221, 1)',
                    bg_city == 'rgba(209, 231, 221, 1)',
                    bg_country == 'rgba(209, 231, 221, 1)',
                    bg_email == 'rgba(209, 231, 221, 1)',
                    bg_phone == 'rgba(209, 231, 221, 1)',
                    bg_jobposition == 'rgba(209, 231, 221, 1)',
                    bg_company == 'rgba(209, 231, 221, 1)']
    driver.quit()
